<script>
	import './layout.css';
	import { Toaster } from 'svelte-sonner';
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
		<li class="cursor-pointer text-white hover:text-yellow-400" alt="tutorial" href="/tutorial/">
			<a href="/tutorial/">Tutorial</a>
		</li>
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/cube-table/">Cubeshop</a>
		</li>
	</ul>
</nav>

<section class="content flex-1">{@render children()}</section>

<!-- footer -->
<div class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/add-product/">admin-only</a>
		</li>
	</ul>
</div>
