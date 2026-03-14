<script>
	import { onMount } from 'svelte';
	import { page } from '$app/state';

	const id = page.params.id;
	let order = $state(null);

	onMount(async () => {
		const res = await fetch(`/api/order/${id}`);
		if (res.ok) order = await res.json();
	});
</script>

{#if order}
	<a href="/orders/" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Orders</a>
	<h1 class="my-8 text-center text-3xl font-bold">Order #{order.id} — {order.customer_name}</h1>

	<div class="mt-6 flex justify-center">
		<div class="w-full max-w-2xl">
			<table class="w-full border-collapse">
				<thead class="bg-gray-500 text-white">
					<tr>
						<th class="px-4 py-2 text-left">Product</th>
						<th class="px-4 py-2 text-left">Price</th>
						<th class="px-4 py-2 text-left">Qty</th>
						<th class="px-4 py-2 text-left">Subtotal</th>
					</tr>
				</thead>
				<tbody>
					{#each order.items as item}
						<tr class="border-b border-gray-200">
							<td class="px-4 py-2">{item.product_name}</td>
							<td class="px-4 py-2">{item.price != null ? `sFr. ${item.price.toFixed(2)}` : '—'}</td>
							<td class="px-4 py-2">{item.quantity}</td>
							<td class="px-4 py-2">sFr. {item.subtotal.toFixed(2)}</td>
						</tr>
					{/each}
				</tbody>
				<tfoot>
					<tr class="font-bold">
						<td colspan="3" class="px-4 py-2 text-right">Total</td>
						<td class="px-4 py-2">sFr. {order.total.toFixed(2)}</td>
					</tr>
				</tfoot>
			</table>
		</div>
	</div>
{/if}
