<script>
	import { onMount } from 'svelte';

	let product = $state([]); // gets tracked now
	let productType = $state('');
	const filteredproduct = $derived(product.filter((product) => product.category == productType));

		getAllproduct();
	});
</script>

<h1 class="my-8 text-center text-3xl font-bold">All Orders</h1>
<div class="mt-4 flex gap-3">
	<button
		class="rounded bg-gray-500 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '3x3';
		}}
	>
		3x3
	</button>
	<button
		class="rounded bg-gray-500 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '4x4';
		}}
	>
		4x4
	</button>
	<button
		class="rounded bg-gray-500 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '2x2';
		}}
	>
		2x2
	</button>
</div>

<!-- Tabelle -->
<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-500 text-white">
		<tr>
			<th class="px-4 py-2 text-left">Name</th>
			<th class="px-4 py-2 text-left">Size</th>
			<th class="px-4 py-2 text-left">Magnetic</th>
			<th class="px-4 py-2 text-left">Category</th>
		</tr>
	</thead>
	<tbody>
		{#each filteredproduct as product}
			<tr class="border-b border-gray-200 hover:bg-gray-100">
				<td class="px-4 py-2">{product.name}</td>
				<td class="px-4 py-2">{product.size}</td>
				<td class="px-4 py-2">{product.magnetic}</td>
				<td class="px-4 py-2">{product.category}</td>
			</tr>
		{/each}
	</tbody>
</table>
