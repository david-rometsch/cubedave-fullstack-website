<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { cart, addToCart } from '$lib/cart.svelte.js';
	import { products, filter, loadProducts } from '$lib/products.svelte.js';

	let quantities = $state({}); // per-product selected quantity

	// Categories not explicitly listed fall under 'others'
	const known = ['3x3', '4x4', '2x2'];

	// Re-computed whenever product list or active filter changes
	const filteredProducts = $derived(
		filter.type === ''
			? products
			: filter.type === 'others'
				? products.filter((p) => !known.includes(p.category))
				: products.filter((p) => p.category == filter.type)
	);

	onMount(loadProducts);
</script>

<h1 class="my-8 text-center text-3xl font-bold">CubeDave's Cube Knowledge</h1>
<div class="mx-auto max-w-prose">
	<h2 class="text-center text-xl font-bold">Magnetic vs. Non-Magnetic</h2>
	<p class="text-justify text-base">
		Nowadays most of the speedcubes have magnets These magnets help you to align the Layers. Cubes
		with magnets are yust slightley more expensive so I would give a clear recommandation to buy a
		Cube with magnets, even if you are a beginner.
	</p>
	<hr class="my-8 border-gray-300" />
	<h2 class="text-center text-xl font-bold">Cornercutting</h2>
	<p class="text-justify text-base">
		Cornercutting is .... body text body text body body text body text body text body text body body
		text body text body text body text body
	</p>
	<hr class="my-8 border-gray-300" />
</div>
