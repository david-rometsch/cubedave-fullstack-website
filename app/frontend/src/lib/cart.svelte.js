export const cart = $state([]);

export function clearCart() {
	cart.splice(0, cart.length);
}
