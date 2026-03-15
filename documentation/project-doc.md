# CubeDave's Cube Shop – Web Engineering Full Stack

**Live:** https://cubedave.ch

---

# 1. Architecture Overview

## 1.1 Full-Stack Layers

```
Browser (SvelteKit SPA)
        ↓  HTTPS / REST
Nginx (Reverse Proxy + SSL termination)
        ↓  HTTP (Docker internal network)
    ┌───────────────────┐
    │  Static files      │  ← compiled Svelte build served by Nginx
    └───────────────────┘
        ↓  /api/* proxied to
FastAPI (Python, Uvicorn)
        ↓  SQLAlchemy ORM
SQLite (database.db)
```

## 1.2 Technology Stack

| Layer | Technology | Role |
|---|---|---|
| Frontend | SvelteKit 5 + Tailwind CSS 4 | SPA, UI, routing |
| Backend | FastAPI + Uvicorn | REST API, business logic |
| ORM | SQLAlchemy | DB abstraction |
| Database | SQLite | Persistence |
| Proxy | Nginx + nginx-certbot | SSL, reverse proxy, static serving |
| Containerisation | Docker + Docker Compose | Deployment |

## 1.3 Separation of Concerns

- **Content:** HTML templates in `.svelte` files
- **Presentation:** Tailwind utility classes, `layout.css`
- **Behaviour:** `$state`, `$derived`, event handlers in `<script>`
- **Data:** `lib/api.js` → `lib/products.svelte.js` / `cart.svelte.js`
- **Server logic:** `main.py` routes, `models.py`, `database.py`

---

# 2. Project Structure

**Backend**
```
app/
├── main.py               # FastAPI routes + startup seeding
├── models.py             # ORM models + Pydantic schemas
├── database.py           # Engine, session factory, get_db
├── test_main.py          # pytest test suite
├── Dockerfile            # Backend container (python:3.12-slim)
├── docker-compose.yaml   # Multi-service orchestration
└── static/
    ├── product.json          # live seed data
    └── product_default.json  # restore baseline
```

**Frontend**
```
frontend/
├── Dockerfile        # Multi-stage: Node build → nginx-certbot
├── nginx.conf        # Reverse proxy + SSL config
├── svelte.config.js  # adapter-static, SPA fallback
└── src/
    ├── routes/
    │   ├── (main)/        # public shop
    │   │   ├── /                    # product list
    │   │   ├── product/[id]/        # detail view
    │   │   └── shopping-cart/       # cart + checkout
    │   └── (admin)/       # admin area
    │       ├── product-list/
    │       ├── add-product/
    │       ├── update-product/
    │       └── orders/[id]/
    └── lib/
        ├── api.js               # fetch wrappers
        ├── products.svelte.js   # global product store + cache
        └── cart.svelte.js       # global cart store
```

---

# 3. CSS & Tailwind

## 3.1 Tailwind Basics

- utility-first CSS framework
- no custom CSS classes needed → compose styles inline
- `@import 'tailwindcss'` in `layout.css` (Tailwind v4 syntax)
- plugins: `@tailwindcss/forms`, `@tailwindcss/typography`

## 3.2 Application in this Project

- dark navbar: `bg-gray-900 px-6 py-3`
- responsive buttons: `rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400`
- brand colour: yellow-400 for highlights, badges, hover states
- table styling: `border-collapse`, `hover:bg-gray-100`, `border-b border-gray-200`
- cart badge in nav: live count via `cart.length` reactive binding

## 3.3 Tailwind vs. plain CSS

| Tailwind | Plain CSS |
|---|---|
| styles directly in markup | separate stylesheet |
| no naming needed | class naming required (BEM etc.) |
| purges unused CSS at build | manual cleanup |
| consistent design tokens | custom variables |

---

# 4. Svelte Basics

## 4.1 What is Svelte

- compile-time framework: ships no runtime, compiles to vanilla JS
- vs. React: React ships ~40 KB runtime + virtual DOM diffing; Svelte has zero runtime overhead

## 4.2 Svelte 5 Runes

Runes are compiler directives that replace the old Svelte store API.

| Rune | Purpose | Used in project |
|---|---|---|
| `$state` | reactive variable | `cart`, `products`, `filter`, `quantities` |
| `$derived` | computed from state | `filteredproduct` in shop page |
| `$props` | component props | `let { children } = $props()` in layouts |
| `$effect` | side-effects on state change | (not used, `onMount` preferred) |

### `$state` example (cart.svelte.js)
```js
export const cart = $state([]);   // reactive array, shared globally
```

### `$derived` example (shop page)
```js
const filteredproduct = $derived(
    filter.type === '' ? products : products.filter(p => p.category === filter.type)
);
// re-computed automatically whenever products or filter.type changes
```

## 4.3 Svelte Stores (Rune-based)

- `products.svelte.js` — global product cache, shared across routes
- `cart.svelte.js` — global cart state, survives navigation
- exported from `lib/` → imported by any component
- no Svelte `writable()`/`readable()` needed in Svelte 5: `$state` at module level acts as store

## 4.4 SvelteKit Routing

- file-based routing: folder = URL segment
- route groups `(main)` / `(admin)`: share layout without affecting URL
- `+layout.svelte`: wraps all child routes (nav, footer, CSS)
- `[id]`: dynamic segment → `product/3` → `params.id = 3`
- `adapter-static`: compiles to static files + `index.html` SPA fallback

---

# 5. REST API & Web Protocols

## 5.1 Web Protocol

- HTTP/HTTPS: request–response protocol
- methods: GET (read), POST (create), PUT (full update), DELETE (remove)
- no PATCH used → updates go through PUT with full object (`/api/update_product/{id}`)
- status codes: 200 OK, 422 Unprocessable Entity (Pydantic validation fail)

## 5.2 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/all_product` | All products |
| POST | `/api/add_product` | Add product |
| PUT | `/api/update_product/{id}` | Update product (full) |
| DELETE | `/api/delete_product/{id}` | Delete product |
| POST | `/api/order` | Create order with line items |
| GET | `/api/orders` | All orders with totals |
| GET | `/api/order/{id}` | Single order + items |
| POST | `/api/visit` | Record a shop visit |
| GET | `/api/visits` | Total visit count |
| POST | `/api/save_data` | Persist DB → product.json |
| POST | `/api/restore_data` | Reset to default products |

## 5.3 FastAPI Features Used

- automatic Swagger docs at `/docs`
- `Depends(get_db)` for dependency injection of DB session
- `response_model=list[ProductSchema]` for automatic serialisation + validation
- Pydantic schemas validate input and standardise JSON output

---

# 6. AJAX Loading

## 6.1 Concept

- AJAX = Asynchronous JavaScript And XML (today: JSON)
- fetch data in background → update DOM without full page reload
- SPA behaviour: Svelte handles routing client-side, only data fetched from server

## 6.2 Implementation

- `api.js`: centralised `fetch('/api/...')` calls
- `onMount(loadProducts)`: fetch on component mount, not on page load
- `loadProducts()` checks cache first: only fetches if `products.length === 0`
- after `addToCart` → toast notification appears without any page reload
- visit tracking: `fetch('/api/visit', { method: 'POST' })` silently in background on shop load

## 6.3 Products Example

```js
// products.svelte.js
export async function loadProducts() {
    if (products.length === 0) {       // cache check
        const data = await fetchProducts();
        products.push(...data);         // triggers re-render of all subscribers
    }
}
```

---

# 7. Database & ORM

## 7.1 SQLAlchemy ORM

- ORM = Object-Relational Mapper: Python classes ↔ DB tables
- no raw SQL needed
- `Base.metadata.create_all(engine)` creates tables from model definitions

## 7.2 Database Models

| Model | Table | Key Fields |
|---|---|---|
| `Product` | `products` | id, name, size, brand, category, price, image (base64) |
| `Order` | `orders` | id, customer_name |
| `ProductOrder` | `product_orders` | product_id (FK), order_id (FK), quantity |
| `Visit` | `visits` | id, visited_at (datetime UTC) |

## 7.3 Association Model with Quantity

- `ProductOrder` = many-to-many between `Product` and `Order`
- carries extra data: `quantity` column
- pure join table couldn't hold quantity → explicit association class needed

```
Order 1 ──── * ProductOrder * ──── 1 Product
                  quantity
```

## 7.4 Pydantic Schemas

| Schema | Purpose |
|---|---|
| `ProductCreateSchema` | validates POST body (no id) |
| `ProductSchema` | extends with id, used for PUT + responses |
| `OrderRequest` | validates order POST: customer_name + items list |

- `model_config = ConfigDict(from_attributes=True)` → allows ORM object → Pydantic conversion
- FastAPI uses `response_model` to auto-serialise + strip unwanted fields

## 7.5 Session Management

- `database.py` owns engine + session factory
- `get_db()`: dependency-injected session per request, auto-closes after response
- `get_session()`: context manager for non-route code (seeding, restore)

---

# 8. Testing

## 8.1 Setup

- framework: `pytest`
- HTTP client: `fastapi.testclient.TestClient` (no server needed)
- DB: in-memory SQLite with `StaticPool` (all connections share same DB)
- dependency override: `app.dependency_overrides[get_db] = override_get_db`

## 8.2 Test Cases

| Test | What it tests |
|---|---|
| `test_add_and_list_product` | POST product → appears in GET all |
| `test_delete_product` | POST product → DELETE → not in GET all |
| `test_create_and_fetch_order` | POST order → GET order returns correct total |
| `test_visit_counter` | 2x POST visit → GET visits returns count=2 |

## 8.3 Run Tests

```bash
source .venv/bin/activate
pytest test_main.py -v
```

## 8.4 Why StaticPool

- `sqlite:///:memory:` creates a new empty DB per connection by default
- `StaticPool` forces all connections to reuse one connection → tables created in fixture are visible to the test session

---

# 9. Security

## 9.1 HTTPS & SSL

- all HTTP traffic redirected to HTTPS (nginx: `return 301 https://...`)
- SSL certificate: Let's Encrypt via Certbot
- base image: `jonasal/nginx-certbot` handles automatic cert renewal
- certs stored in Docker volume `letsencrypt` (persists across restarts)

### nginx.conf flow
```
HTTP :80  →  301 redirect  →  HTTPS :443
HTTPS :443
  /           →  static Svelte build
  /api/*      →  proxy_pass fastapi:8000
  /docs       →  proxy_pass fastapi:8000
```

## 9.2 Pydantic Validation

- all API inputs validated by Pydantic schemas before reaching business logic
- wrong types / missing required fields → automatic 422 response
- `response_model` on GET routes → controls exactly what JSON is returned (no accidental field leaks)

---

# 10. Performance

## 10.1 Svelte Compilation vs. React

| | Svelte | React |
|---|---|---|
| Runtime shipped to browser | none (compiles away) | ~40–45 KB (react + react-dom) |
| DOM updates | direct DOM manipulation, compiled | virtual DOM diffing |
| Bundle size | small | larger baseline |
| Reactivity | compiler-tracked | hooks + re-render cycle |

## 10.2 Product Store – Fetch Once, Cache

- `products` is module-level `$state` → survives navigation within the SPA
- `loadProducts()` guards with `if (products.length === 0)`
- first visit: fetches from `/api/all_product`
- subsequent navigation back to shop: instant render from cache, zero network request
- invalidation after add-product: `invalidateProducts()` splices the array → next load re-fetches

## 10.3 Filter Without Re-fetch

- `filter.type` is `$state` in the same module
- category filter computed via `$derived` → no API call, pure client-side filtering
- filter state persists when navigating to detail page and back

---

# 11. Docker & Deployment

## 11.1 Containers

| Service | Image | Role |
|---|---|---|
| `fastapi` | custom (python:3.12-slim) | FastAPI + Uvicorn on :8000 |
| `nginx-svelte` | jonasal/nginx-certbot + static build | Nginx on :80/:443, certbot |

## 11.2 Frontend Multi-Stage Build

```dockerfile
# Stage 1: compile SvelteKit → static files
FROM node:20 AS builder
RUN npm install && npm run build

# Stage 2: serve
FROM jonasal/nginx-certbot
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
```

- Stage 1 produces static HTML/JS/CSS in `/app/build`
- Stage 2 ships only the compiled output — no Node.js in production image

## 11.3 Backend Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install "fastapi[standard]" sqlalchemy
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 11.4 Deploy Commands

```bash
# build and start
docker compose up -d --build

# view logs
docker compose logs -f
```

---

# Reflection

<!-- Write your own reflection here -->
