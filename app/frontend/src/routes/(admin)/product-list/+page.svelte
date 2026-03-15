<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { toast } from 'svelte-sonner';
	import { fetchProducts } from '$lib/api.js';
	import { invalidateProducts } from '$lib/products.svelte.js';

	let products = $state([]);
	let productType = $state('');

	// Re-computed whenever the filter or product list changes
	const filteredproduct = $derived(
		productType === '' ? products : products.filter((p) => p.category == productType)
	);

	onMount(async () => {
		products = await fetchProducts();
	});
</script>

<h1 class="my-8 text-center text-3xl font-bold">All Products</h1>

<!-- Category filter buttons -->
<div class="mt-4 flex gap-3">
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { productType = ''; }}
	>all</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { productType = '3x3'; }}
	>3x3</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { productType = '4x4'; }}
	>4x4</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { productType = '2x2'; }}
	>2x2</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { productType = 'others'; }}
	>others</button>
</div>

<!-- Product table with update and delete actions -->
<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-500 text-white">
		<tr>
			<th class="px-4 py-2 text-left">Image</th>
			<th class="px-4 py-2 text-left">Name</th>
			<th class="px-4 py-2 text-left">Size</th>
			<th class="px-4 py-2 text-left">Info</th>
			<th class="px-4 py-2 text-left">Category</th>
			<th class="px-4 py-2 text-left">Price</th>
			<th class="px-4 py-2 text-left">Action</th>
		</tr>
	</thead>
	<tbody>
		{#each filteredproduct as p}
			<tr class="border-b border-gray-200 hover:bg-gray-100">
				<td class="px-4 py-2">
					{#if p.image}
						<img src={p.image} alt={p.name} style="width:57px;height:57px;object-fit:contain;" />
					{:else}
						<span class="text-sm text-gray-400">kein Bild</span>
					{/if}
				</td>
				<td class="px-4 py-2">{p.name}</td>
				<td class="px-4 py-2">{p.size}</td>
				<td class="px-4 py-2">{p.info}</td>
				<td class="px-4 py-2">{p.category}</td>
				<td class="px-4 py-2">{p.price ?? '—'}</td>
				<td class="px-4 py-2">
					<div class="flex gap-2">
						<button
							class="w-20 rounded bg-gray-800 px-2 py-1 text-sm text-white transition hover:bg-yellow-400 hover:text-gray-900"
							onclick={() => goto(`/update-product/?id=${p.id}`)}
						>update</button>
						<!-- Delete removes the product from the DB and updates the local list reactively -->
						<button
							class="w-20 rounded bg-red-700 px-2 py-1 text-sm text-white transition hover:bg-yellow-400 hover:text-gray-900"
							onclick={async () => {
								const res = await fetch(`/api/delete_product/${p.id}`, { method: 'DELETE' });
								if (res.ok) {
									products = products.filter((x) => x.id !== p.id);
									invalidateProducts();
									toast.success('Product deleted!');
								} else {
									toast.error('Error!');
								}
							}}
						>delete</button>
					</div>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
