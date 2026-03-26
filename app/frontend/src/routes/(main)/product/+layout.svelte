<script>
	import { cart } from '$lib/cart.svelte.js';

	let { children } = $props();
</script>

<!-- 2nd navbar: shop title + cart badge -->
<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="text-2xl font-bold text-yellow-400">Get Cubes at CubeDave's Cube Shop</li>
		<li class="ml-auto">
			<a
				href="/shopping-cart"
				class="rounded bg-yellow-400 px-4 py-2 font-bold text-gray-900 transition hover:bg-yellow-300"
			>
				Cart ({cart.length})
			</a>
		</li>
	</ul>
</nav>

{@render children()}
