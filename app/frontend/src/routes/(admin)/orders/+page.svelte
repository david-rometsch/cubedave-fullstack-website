<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	let orders = $state([]);

	onMount(async () => {
		const res = await fetch('/api/orders');
		if (res.ok) orders = await res.json();
	});
</script>

<h1 class="my-8 text-center text-3xl font-bold">All Orders</h1>

<table class="mt-6 w-full border-collapse">
	<thead class="bg-gray-500 text-white">
		<tr>
			<th class="px-4 py-2 text-left">#</th>
			<th class="px-4 py-2 text-left">Customer</th>
			<th class="px-4 py-2 text-left">Total</th>
			<th class="px-4 py-2 text-left"></th>
		</tr>
	</thead>
	<tbody>
		{#each orders as o}
			<tr class="border-b border-gray-200 hover:bg-gray-100">
				<td class="px-4 py-2">{o.id}</td>
				<td class="px-4 py-2">{o.customer_name}</td>
				<td class="px-4 py-2">sFr. {o.total.toFixed(2)}</td>
				<td class="px-4 py-2">
					<!-- Navigate to dynamic order detail route -->
					<button
						class="rounded bg-gray-800 px-3 py-1 text-sm text-white transition hover:bg-yellow-400 hover:text-gray-900"
						onclick={() => goto(`/orders/${o.id}`)}
					>detail</button>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
