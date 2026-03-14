<script>
	import { onMount } from 'svelte';
	import { cart, clearCart } from '$lib/cart.svelte.js'; // needed for transient order items on multiple pages

	let product = $state([]); // gets tracked now
	let productType = $state('');
	const filteredproduct = $derived(
		productType === '' ? product : product.filter((p) => p.category == productType)
	);

	// fetch product from BE
	onMount(() => {
		async function getAllproduct() {
			let responseJson = '';
			try {
				let response = await fetch('/api/all_product');
				if (!response.ok) throw new Error(`HTTP Fehler! Status: ${response.status}`);
				responseJson = await response.json();
				// console.log(`product: ${product}`);
				console.log(`response json: ${responseJson}`);
				product = responseJson;
			} catch (err) {
				// output.textContent = "Fehler: " + err.message
				// console.error('Fetch-Fehler:', err);
			}
		}
		getAllproduct();
	});
</script>

<h1 class="my-8 text-center text-3xl font-bold">Gear Up To Be Fast!</h1>
<div class="mt-4 flex gap-3">
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '';
		}}
	>
		all
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '3x3';
		}}
	>
		3x3
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '4x4';
		}}
	>
		4x4
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = '2x2';
		}}
	>
		2x2
	</button>
	<button
		class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
		onclick={() => {
			productType = 'others';
		}}
	>
		others
	</button>
</div>

<!-- Tabelle -->
<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-800 text-white">
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
