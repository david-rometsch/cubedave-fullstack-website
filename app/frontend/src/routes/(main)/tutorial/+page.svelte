<script>
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import { addToCart } from '$lib/cart.svelte.js';
	import { products, loadProducts } from '$lib/products.svelte.js';

	// Read dynamic route segment — e.g. /product/3 → id = "3"
	const id = page.params.id;
	let quantity = $state(1);

	onMount();
</script>

<!-- <a href="/" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Shop</a> -->
<h1 class="my-8 text-center text-3xl font-bold">Learn how to Be Fast!</h1>
<hr class="my-8 border-gray-300" />
