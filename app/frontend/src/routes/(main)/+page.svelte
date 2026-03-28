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

<h1 class="my-8 text-center text-3xl font-bold">Welcome to CubeDave!</h1>
<div class="mx-auto max-w-prose">
	<p class="text-justify text-base">
		I am David, I am a cuber and a teacher and a Cubing-Teacher and this is my site about various
		aspects of cubing. I recommand for beginners to watch the solve, then head over to <a
			href="cube-knowledge"
			class="text-blue-600 hover:text-blue-800">Cube Knowledge</a
		>
		and finally visit the <a href="shop" class="text-blue-600 hover:text-blue-800">shop</a>!

		<a href="/" class="block text-right text-blue-600 hover:text-blue-800">read more -></a>
	</p>

	<!-- <video src="images/solve-mute.mp4" muted autoplay loop playsinline></video> -->
	<video
		src="images/solve-mute.mp4"
		muted
		controls
		playsinline
		preload="auto"
		class="w-full"
	></video>
		<a href="/product/2" class="block text-right text-blue-600 hover:text-blue-800">Get this cube at the shop!</a>
</div>
