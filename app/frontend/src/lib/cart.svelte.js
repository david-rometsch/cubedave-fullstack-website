export const cart = $state([]); // [{product, quantity}]

export function addToCart(product, quantity = 1) {
	const existing = cart.find((item) => item.product.id === product.id);
	if (existing) {
		existing.quantity += quantity;
	} else {
		cart.push({ product, quantity });
	}
}

export function clearCart() {
	cart.splice(0, cart.length);
}
