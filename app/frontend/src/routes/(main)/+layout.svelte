<script>
	import { onMount } from 'svelte';
	import '../layout.css';
	import { Toaster } from 'svelte-sonner';
	import { cart } from '$lib/cart.svelte.js';

	let { children } = $props();

	// Record a visit each time the shop is loaded
	onMount(() => {
		fetch('/api/visits', { method: 'POST' });
	});
</script>

<!-- Toast notification container -->
<Toaster />

<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="mr-auto">
			<a href="/">
				<img
					class="h-10 w-10 rounded-full object-cover"
					alt="cubes-logo"
					src="/images/cube.jpg"
				/>
			</a>
		</li>
		<li class="text-yellow-400"><a href="/tutorial">Tutorial</a></li>
		<li class="text-yellow-400"><a href="/cube-knowledge">Cube Knowledge</a></li>
		<li class="text-yellow-400"><a href="/product/shop">Shop</a></li>
	</ul>
</nav>

<section class="content flex-1 overflow-x-auto">{@render children()}</section>

<!-- Footer with hidden admin link -->
<div class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/product-list/">admin-only</a>
		</li>
	</ul>
</div>
