<script>
	import '../layout.css';
	import { Toaster, toast } from 'svelte-sonner';

	let { children } = $props();
</script>

<!-- Toast notification container -->
<Toaster />

<nav class="bg-gray-300 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li>
			<a href="/" class="rounded bg-gray-900 px-4 py-2 text-white hover:text-yellow-400">Shop</a>
		</li>
		<li class="ml-auto cursor-pointer text-gray-800 hover:text-yellow-400">
			<a href="/orders/">Orders</a>
		</li>
		<li class="cursor-pointer text-gray-800 hover:text-yellow-400">
			<a href="/product-list/">Product List</a>
		</li>
		<li class="cursor-pointer text-gray-800 hover:text-yellow-400">
			<a href="/add-product/">Add Product</a>
		</li>
	</ul>
</nav>

<section class="content flex-1">{@render children()}</section>

<!-- Footer: persists current DB state back to the seed file -->
<div class="bg-gray-300 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li>
			<button
				class="cursor-pointer text-gray-800 hover:text-yellow-400"
				onclick={async () => {
					const res = await fetch('/api/save_data', { method: 'POST' });
					if (res.ok) toast.success('Daten gespeichert');
					else toast.error('Fehler beim Speichern');
				}}
			>
				Save Demo Data
			</button>
		</li>
	</ul>
</div>
