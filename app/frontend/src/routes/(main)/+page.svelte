<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { cart, addToCart } from '$lib/cart.svelte.js';
	import { products, filter, loadProducts } from '$lib/products.svelte.js';

	let quantities = $state({});  // per-product selected quantity

	// Categories not explicitly listed fall under 'others'
	const known = ['3x3', '4x4', '2x2'];

	// Re-computed whenever product list or active filter changes
	const filteredproduct = $derived(
		filter.type === ''
			? products
			: filter.type === 'others'
				? products.filter((p) => !known.includes(p.category))
				: products.filter((p) => p.category == filter.type)
	);

	onMount(loadProducts);
</script>

<h1 class="my-8 text-center text-3xl font-bold">Gear Up To Be Fast!</h1>

<!-- Category filter buttons -->
<div class="mt-4 flex gap-3">
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { filter.type = ''; }}
	>
		all
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { filter.type = '3x3'; }}
	>
		3x3
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { filter.type = '4x4'; }}
	>
		4x4
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { filter.type = '2x2'; }}
	>
		2x2
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => { filter.type = 'others'; }}
	>
		others
	</button>
</div>

<!-- Product table — clicking a row navigates to the detail view -->
<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-800 text-white">
		<tr>
			<th class="px-4 py-2 text-left">Image</th>
			<th class="px-4 py-2 text-left">Name</th>
			<th class="px-4 py-2 text-left">Size</th>
			<th class="px-4 py-2 text-left">Info</th>
			<th class="px-4 py-2 text-left">Category</th>
			<th class="px-4 py-2 text-left">Price</th>
			<th class="px-4 py-2 text-left">Qty</th>
			<th class="px-4 py-2 text-left"></th>
		</tr>
	</thead>
	<tbody>
		{#each filteredproduct as product}
			<tr class="cursor-pointer border-b border-gray-200 hover:bg-gray-100" onclick={() => goto(`/product/${product.id}`)}>
				<td class="px-4 py-2">
					{#if product.image}
						<img src={product.image} alt={product.name} style="width:57px;height:57px;object-fit:contain;" />
					{:else}
						<span class="text-sm text-gray-400">kein Bild</span>
					{/if}
				</td>
				<td class="px-4 py-2">{product.name}</td>
				<td class="px-4 py-2">{product.size}</td>
				<td class="px-4 py-2">{product.info}</td>
				<td class="px-4 py-2">{product.category}</td>
				<td class="px-4 py-2">{product.price != null ? `sFr. ${product.price.toFixed(2)}` : '—'}</td>
				<td class="px-4 py-2">
					<!-- stopPropagation prevents the row click from firing when using the select -->
					<select
						class="w-14 rounded border border-gray-300 py-1 pl-2 pr-6"
						bind:value={quantities[product.id]}
						onclick={(e) => e.stopPropagation()}
					>
						{#each [1,2,3,4,5,6,7,8,9,10] as n}
							<option value={n}>{n}</option>
						{/each}
					</select>
				</td>
				<td class="px-4 py-2">
					<!-- stopPropagation prevents navigation to detail view when clicking add -->
					<button
						class="rounded bg-gray-800 px-3 py-1 text-sm text-white transition hover:bg-yellow-400 hover:text-gray-900"
						onclick={(e) => { e.stopPropagation(); addToCart(product, quantities[product.id] ?? 1); }}
					>add</button>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
