/**
 * products.svelte.js — Reactive global store for products and category filter.
 * Fetches once on first load; subsequent navigations reuse the cached data.
 */

import { fetchProducts } from '$lib/api.js';

/** Cached product list — shared across all components */
export const products = $state([]);

/** Active category filter — persists when navigating away and back */
export const filter = $state({ type: '' });

/**
 * Load products from the API only if not already cached.
 * Call this in onMount on any page that needs the product list.
 */
export async function loadProducts() {
	if (products.length === 0) {
		const data = await fetchProducts();
		products.push(...data);
	}
}
