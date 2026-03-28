<script>
	import { onMount } from 'svelte';
	import '../layout.css';
	import { Toaster } from 'svelte-sonner';
	import { cart } from '$lib/cart.svelte.js';
	import { beforeNavigate } from '$app/navigation';
	import { nav } from '$lib/nav.svelte.js';

	let { children } = $props();

	beforeNavigate(({ from }) => {
		nav.prev = from?.url.pathname ?? null;
	});

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
		<li class="relative ml-auto">
			<a href="/shopping-cart" class="flex items-center rounded bg-yellow-400 p-2 transition hover:bg-yellow-300">
				<img src="/images/cart.png" alt="Cart" class="h-6 w-6" />
			</a>
			<span class="absolute -top-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full bg-gray-900 text-xs font-bold text-yellow-400">
				{cart.length}
			</span>
		</li>
	</ul>
</nav>

<section class="content flex-1 overflow-x-auto">{@render children()}</section>

<!-- Footer -->
<div class="bg-gray-900 px-6 py-3">
	<div class="flex items-center">
		<a href="/product-list/" class="text-xs text-gray-600 hover:text-gray-400">admin-only</a>
		<ul class="flex flex-1 justify-center gap-6">
			<li><a href="#" class="text-yellow-400 hover:text-yellow-300">Impressum</a></li>
			<li><span class="text-gray-600">|</span></li>
			<li><a href="#" class="text-yellow-400 hover:text-yellow-300">Contact</a></li>
			<li><span class="text-gray-600">|</span></li>
			<li><a href="#" class="text-yellow-400 hover:text-yellow-300">Links</a></li>
		</ul>
	</div>
</div>
