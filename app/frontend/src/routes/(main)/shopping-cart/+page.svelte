<script>
	import { cart, clearCart } from '$lib/cart.svelte.js';
	import { toast } from 'svelte-sonner';
	import { goto } from '$app/navigation';

	let customerName = $state('');

	const total = $derived(
		cart.reduce((sum, item) => sum + (item.product.price ?? 0) * item.quantity, 0)
	);

	async function confirmOrder() {
		if (!customerName.trim()) {
			toast.error('Please enter your name first.');
			return;
		}
		const res = await fetch('/api/order', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				customer_name: customerName,
				items: cart.map((item) => ({ product_id: item.product.id, quantity: item.quantity }))
			})
		});
		if (res.ok) {
			toast.success('Order placed!');
			clearCart();
			goto('/');
		} else {
			toast.error('Error placing order!');
		}
	}
</script>

<a href="/" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Shop</a>

<h1 class="my-8 text-center text-3xl font-bold">Shopping Cart</h1>

{#if cart.length === 0}
	<p class="mt-8 text-center text-gray-400">Cart is empty.</p>
{:else}
	<div class="mt-6 flex justify-center">
		<div class="w-full max-w-2xl">
			<table class="w-full border-collapse">
				<thead class="bg-gray-800 text-white">
					<tr>
						<th class="px-4 py-2 text-left">Product</th>
						<th class="px-4 py-2 text-left">Price</th>
						<th class="px-4 py-2 text-left">Qty</th>
						<th class="px-4 py-2 text-left">Subtotal</th>
					</tr>
				</thead>
				<tbody>
					{#each cart as item}
						<tr class="border-b border-gray-200">
							<td class="px-4 py-2">{item.product.name}</td>
							<td class="px-4 py-2">{item.product.price != null ? `sFr. ${item.product.price.toFixed(2)}` : '—'}</td>
							<td class="px-4 py-2">
								<select
									class="w-14 rounded border border-gray-300 py-1 pl-2 pr-6"
									bind:value={item.quantity}
								>
									{#each [1,2,3,4,5,6,7,8,9,10] as n}
										<option value={n}>{n}</option>
									{/each}
								</select>
							</td>
							<td class="px-4 py-2">
								{item.product.price != null ? `sFr. ${(item.product.price * item.quantity).toFixed(2)}` : '—'}
							</td>
						</tr>
					{/each}
				</tbody>
				<tfoot>
					<tr class="font-bold">
						<td colspan="3" class="px-4 py-2 text-right">Total</td>
						<td class="px-4 py-2">sFr. {total.toFixed(2)}</td>
					</tr>
				</tfoot>
			</table>

			<!-- customer name -->
			<div class="mt-6 flex items-center gap-3">
				<label class="w-36 text-right text-sm font-bold text-gray-700">Name</label>
				<input
					type="text"
					bind:value={customerName}
					placeholder="Your name"
					class="w-64 rounded border-2 border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
				/>
			</div>

			<!-- buttons -->
			<div class="mt-6 mb-8 flex gap-4">
				<button
					class="rounded bg-slate-400 px-4 py-2 text-white transition hover:bg-gray-900"
					onclick={() => { clearCart(); goto('/'); }}
				>cancel</button>
				<button
					class="ml-auto rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
					onclick={confirmOrder}
				>confirm</button>
			</div>
		</div>
	</div>
{/if}
