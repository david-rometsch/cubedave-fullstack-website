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
	<h2 id="magnetic" class="text-center text-xl font-bold">Magnetic vs. Non-Magnetic</h2>
	<p class="text-justify text-base">
		Nowadays most of the speedcubes have magnets These magnets help you to align the Layers. Cubes
		with magnets are yust slightley more expensive so I would give a clear recommandation to buy a
		Cube with magnets, even if you are a beginner.
	</p>
	<hr class="my-8 border-gray-300" />
	<h2 class="text-center text-xl font-bold">Cornercutting</h2>
	<p class="text-justify text-base">
		Cornercutting is the amount of missalingnment, the cube can tolerate and still do the move you
		intended.
	</p>
	<ul>
		<li>
			Foreward cornercutting (or just cornercuttiong)? Here you test to which degree of
			missalignment the Layer will still finish its Move
		</li>
		<li>
			Reverse cornercutting: here you test on which degree of missalignment the layer will snap back
			into the old Position
		</li>
	</ul>
	<hr class="my-8 border-gray-300" />
	<h2 if="maglev" class="text-center text-xl font-bold">MagLev</h2>
	<p class="text-justify text-base">
		MagLev is an upgrade over springs on the center pieces. it reduces friction and noise. Two
		repelling ringshaped magnets are implemented in order to acheive the cussioning easier
	</p>
	<hr class="my-8 border-gray-300" />
	<h2 id="uv" class="text-center text-xl font-bold">UV-Coating</h2>
	<p class="text-justify text-base"></p>
	UV-Coating improves the grip on the cube. A thin extra layer ov UV-coating is applied on the surface
	of the cube.
</div>
