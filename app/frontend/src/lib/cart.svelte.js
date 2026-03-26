/**
 * cart.svelte.js — Reactive global cart state shared across all components.
 * Uses Svelte 5 $state rune so any component reading `cart` re-renders on change.
 */

/** Cart items: array of { product, quantity } */
export const cart = $state([]);

/**
 * Add a product to the cart.
 * If the product is already in the cart, its quantity is incremented instead.
 */
export function addToCart(product, quantity = 1) {
	const existing = cart.find((item) => item.product.id === product.id);
	if (existing) {
		existing.quantity += quantity;
	} else {
		cart.push({ product, quantity });
	}
}

/** Remove a single item from the cart by product id. */
export function removeFromCart(productId) {
	const idx = cart.findIndex((item) => item.product.id === productId);
	if (idx !== -1) cart.splice(idx, 1);
}

/** Remove all items from the cart. */
export function clearCart() {
	cart.splice(0, cart.length);
}
