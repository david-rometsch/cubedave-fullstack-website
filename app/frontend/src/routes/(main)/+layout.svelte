<script>
	import '../layout.css';
	import { Toaster, toast } from 'svelte-sonner';
	import { cart } from '$lib/cart.svelte.js';
	// usage: {@html marked(product.description)}
	let { children } = $props();
</script>

<Toaster />

<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="mr-auto">
			<a href="/">
				<img class="h-10 w-10 rounded-full object-cover" alt="cubes-logo" src="images/cube.jpg" />
			</a>
		</li>
		<!-- <li class="text-2xl font-bold text-yellow-400">Welcome To CubeDave's Cube Shop!</li> -->
		<li class="text-2xl font-bold text-yellow-400">Get Cubes at CubeDave's Cube Shop!</li>
		<li class="ml-auto">
			<a href="/shopping-cart/" class="rounded bg-yellow-400 px-4 py-2 font-bold text-gray-900 transition hover:bg-yellow-300">
				Cart ({cart.length})
			</a>
		</li>

		<!-- <li class="cursor-pointer text-white hover:text-yellow-400" alt="tutorial" href="/tutorial/"> -->
		<!-- 	<a href="/tutorial/">Tutorial</a> -->
		<!-- </li> -->
		<!-- <li class="cursor-pointer text-white hover:text-yellow-400"> -->
		<!-- 	<a href="/shop/">Cubeshop</a> -->
		<!-- </li> -->
	</ul>
</nav>

<section class="content flex-1">{@render children()}</section>

<!-- footer -->
<div class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/product-list/">admin-only</a>
		</li>
	</ul>
</div>
