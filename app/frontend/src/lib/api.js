/**
 * api.js — Centralised API calls to the backend.
 * Import from here instead of calling fetch('/api/...') directly in components.
 */

/** Fetch all products from the backend. */
export async function fetchProducts() {
	const res = await fetch('/api/products');
	if (!res.ok) throw new Error(`HTTP ${res.status}`);
	return res.json();
}
