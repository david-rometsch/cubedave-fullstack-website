/**
 * checkout.svelte.js — Persistent checkout form state.
 * Lives in memory so navigating back to shop and returning keeps the form filled.
 */
export const checkout = $state({
	firstName: '',
	lastName: '',
	email: '',
	address: '',
	zip: '',
	city: '',
	paymentMethod: 'card',
	/** Set after a successful order; used by the confirmation page. */
	confirmedOrder: null
});
