<script>
	import { onMount } from 'svelte';
	import '../layout.css';
	import { Toaster } from 'svelte-sonner';
	import { cart } from '$lib/cart.svelte.js';

	let { children } = $props();

	// Record a visit each time the shop is loaded
	onMount(() => {
		fetch('/api/visit', { method: 'POST' });
	});
</script>

<!-- Toast notification container -->
<Toaster />

<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="mr-auto">
			<a href="/">
				<img class="h-10 w-10 rounded-full object-cover" alt="cubes-logo" src="images/cube.jpg" />
			</a>
		</li>
		<li class="text-2xl font-bold text-yellow-400">Get Cubes at CubeDave's Cube Shop</li>
		<!-- Cart badge shows number of distinct items in cart -->
		<li class="ml-auto">
			<a
				href="/shopping-cart/"
				class="rounded bg-yellow-400 px-4 py-2 font-bold text-gray-900 transition hover:bg-yellow-300"
			>
				Cart ({cart.length})
			</a>
		</li>
	</ul>
</nav>

<section class="content flex-1">{@render children()}</section>

<!-- Footer with hidden admin link -->
<div class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/product-list/">admin-only</a>
		</li>
	</ul>
</div>
