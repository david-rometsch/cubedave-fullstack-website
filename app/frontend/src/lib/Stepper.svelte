<script>
	/**
	 * Renders the correct stepper SVG for the current checkout step,
	 * with transparent clickable overlays on each segment.
	 *
	 * SVG viewBox: 0 0 680 88
	 * Segment x-ranges (approximate, used for overlay positioning):
	 *   Shop:         40–193  → left 5.9%,  width 22.5%
	 *   Cart:        197–350  → left 29%,   width 22.5%
	 *   Checkout:    354–507  → left 52.1%, width 22.5%
	 *   Confirmation:511–636  → left 75.1%, width 18.4%
	 * Click region height: y 22–66 → top 25%, height 50%
	 */
	let { step, passive = false } = $props(); // 'cart' | 'checkout' | 'confirmation'

	const pastOrCurrent = (s) => {
		const order = ['cart', 'checkout', 'confirmation'];
		return order.indexOf(s) <= order.indexOf(step);
	};
</script>

<div class="relative mx-auto transition-opacity {passive ? 'opacity-40 pointer-events-none' : ''}" style="max-width:680px">
	<img
		src="/images/files/stepper-{step}.svg"
		alt="Checkout-Fortschritt"
		class="w-full"
		draggable="false"
	/>

	<!-- Shop — always clickable -->
	<a
		href="/product/shop"
		class="absolute top-1/4 h-1/2 cursor-pointer"
		style="left:5.9%;width:22.5%"
		aria-label="Zum Shop"
	></a>

	<!-- Cart — clickable when past or current step is cart+ -->
	{#if pastOrCurrent('cart')}
		<a
			href="/shopping-cart"
			class="absolute top-1/4 h-1/2 cursor-pointer"
			style="left:29%;width:22.5%"
			aria-label="Zum Warenkorb"
		></a>
	{/if}

	<!-- Checkout — only clickable once reached -->
	{#if pastOrCurrent('checkout')}
		<a
			href="/checkout"
			class="absolute top-1/4 h-1/2 cursor-pointer"
			style="left:52.1%;width:22.5%"
			aria-label="Zur Kasse"
		></a>
	{/if}

	<!-- Confirmation — only clickable once reached -->
	{#if pastOrCurrent('confirmation')}
		<a
			href="/confirmation"
			class="absolute top-1/4 h-1/2 cursor-pointer"
			style="left:75.1%;width:18.4%"
			aria-label="Zur Bestätigung"
		></a>
	{/if}
</div>
