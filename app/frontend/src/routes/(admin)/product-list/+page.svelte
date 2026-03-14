<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	// import { getAllproduct } from '$lib/api.js';

	let product = $state([]); // gets tracked now
	let productType = $state('');
	const filteredproduct = $derived(product.filter((product) => product.category == productType));

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
		// fetch product from BE
		// onMount(async () => {
		// 	product = await getAllProducts();
		// });
	});
</script>

<h1 class="my-8 text-center text-3xl font-bold">All Products</h1>

<!-- Tabelle -->
<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-500 text-white">
		<tr>
			<th class="px-4 py-2 text-left">Name</th>
			<th class="px-4 py-2 text-left">Size</th>
			<th class="px-4 py-2 text-left">Magnetic</th>
			<th class="px-4 py-2 text-left">Category</th>
			<th class="px-4 py-2 text-left">Action</th>
		</tr>
	</thead>
	<tbody>
		{#each product as p}
			<tr class="border-b border-gray-200 hover:bg-gray-100">
				<td class="px-4 py-2">{p.name}</td>
				<td class="px-4 py-2">{p.size}</td>
				<td class="px-4 py-2">{p.magnetic}</td>
				<td class="px-4 py-2">{p.category}</td>
				<td class="px-4 py-2">
					<button
						class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
						onclick={() => goto('/update-product')}
					>
						update
					</button>
				</td>
				<!-- <td><button>change</button></td> -->
			</tr>
		{/each}
	</tbody>
</table>
