"""
test_main.py — pytest test suite for the FastAPI backend.

Uses an in-memory SQLite database so tests are isolated and leave no files behind.
The TestClient from FastAPI allows calling endpoints without a running server.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import get_db
from main import app
from models import Base

# In-memory SQLite engine — StaticPool forces all connections to share the same
# in-memory database, so tables created in the fixture are visible to the session
TEST_ENGINE = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=TEST_ENGINE)


@pytest.fixture(autouse=True)
def setup_db():
    """Create all tables before each test and drop them afterwards."""
    Base.metadata.create_all(TEST_ENGINE)
    yield
    Base.metadata.drop_all(TEST_ENGINE)


def override_get_db():
    """Replaces the real get_db dependency with one using the in-memory database."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Swap out the real DB dependency for the test one
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Minimal valid product payload used across multiple tests
SAMPLE_PRODUCT = {
    "name": "Test Cube",
    "size": "3x3",
    "brand": "GAN",
    "info": None,
    "category": "Speed",
    "price": 29.99,
    "description": "A fast cube",
    "image": None,
}


# ==== Product CRUD ====

def test_add_and_list_product():
    """Adding a product should make it appear in the product list."""
    response = client.post("/api/add_product", json=SAMPLE_PRODUCT)
    assert response.status_code == 200
    product_id = response.json()["id"]

    response = client.get("/api/all_product")
    assert response.status_code == 200
    ids = [p["id"] for p in response.json()]
    assert product_id in ids


def test_delete_product():
    """Deleting a product should remove it from the product list."""
    product_id = client.post("/api/add_product", json=SAMPLE_PRODUCT).json()["id"]

    response = client.delete(f"/api/delete_product/{product_id}")
    assert response.status_code == 200

    ids = [p["id"] for p in client.get("/api/all_product").json()]
    assert product_id not in ids


# ==== Order creation and total calculation ====

def test_create_and_fetch_order():
    """Creating an order should return an order_id, and fetching it should compute the correct total."""
    product_id = client.post("/api/add_product", json=SAMPLE_PRODUCT).json()["id"]

    order_payload = {
        "customer_name": "Alice",
        "items": [{"product_id": product_id, "quantity": 2}],
    }
    response = client.post("/api/order", json=order_payload)
    assert response.status_code == 200
    order_id = response.json()["order_id"]

    response = client.get(f"/api/order/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Alice"
    assert data["total"] == round(SAMPLE_PRODUCT["price"] * 2, 2)


# ==== Visit counter ====

def test_visit_counter():
    """Recording two visits should result in a count of 2."""
    client.post("/api/visit")
    client.post("/api/visit")

    response = client.get("/api/visits")
    assert response.status_code == 200
    assert response.json()["count"] == 2
