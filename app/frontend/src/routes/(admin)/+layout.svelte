<script>
	import '../layout.css';
	import { Toaster } from 'svelte-sonner';
	// usage: {@html marked(product.description)}
	let { children } = $props();
</script>

<Toaster />

<nav class="bg-gray-300 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/">Home</a>
		</li>

		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/orders/">Orders</a>
		</li>

		<li class="cursor-pointer text-white hover:text-yellow-400">
			<a href="/add-product/">Add Product</a>
		</li>
	</ul>
</nav>

<section class="content flex-1">{@render children()}</section>

<!-- footer -->
<div class="bg-gray-300 px-6 py-3">
	<ul class="flex items-center gap-6"></ul>
</div>
