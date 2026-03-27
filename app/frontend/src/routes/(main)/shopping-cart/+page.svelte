<script>
	import { cart, clearCart, removeFromCart } from '$lib/cart.svelte.js';
	import Stepper from '$lib/Stepper.svelte';
	import { goto } from '$app/navigation';

	const total = $derived(
		cart.reduce((sum, item) => sum + (item.product.price ?? 0) * item.quantity, 0)
	);
</script>

<div class="mx-auto max-w-5xl px-6 py-8">
	<Stepper step="cart" />

	<h1 class="my-8 text-center text-3xl font-bold">Shopping Cart</h1>

	{#if cart.length === 0}
		<p class="mt-8 text-center text-gray-400">Your cart is empty.</p>
		<div class="mt-6 text-center">
			<a
				href="/product/shop"
				class="rounded bg-gray-800 px-6 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
			>← Shop</a>
		</div>
	{:else}
		<table class="w-full border-collapse">
			<thead class="bg-gray-800 text-white">
				<tr>
					<th class="px-4 py-2"></th>
					<th class="px-4 py-2 text-left">Product</th>
					<th class="px-4 py-2 text-left">Price</th>
					<th class="px-4 py-2 text-left">Qty</th>
					<th class="px-4 py-2 text-left">Subtotal</th>
					<th class="px-4 py-2"></th>
				</tr>
			</thead>
			<tbody>
				{#each cart as item}
					<tr class="border-b border-gray-200">
						<td class="px-4 py-2">
							{#if item.product.image}
								<img src={item.product.image} alt={item.product.name} class="h-12 w-12 rounded object-contain" />
							{:else}
								<div class="h-12 w-12 rounded bg-gray-100"></div>
							{/if}
						</td>
						<td class="px-4 py-2">{item.product.name}</td>
						<td class="px-4 py-2">
							{item.product.price != null ? `sFr. ${item.product.price.toFixed(2)}` : '—'}
						</td>
						<td class="px-4 py-2">
							<select
								class="w-14 rounded border border-gray-300 py-1 pr-6 pl-2"
								bind:value={item.quantity}
							>
								{#each [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] as n}
									<option value={n}>{n}</option>
								{/each}
							</select>
						</td>
						<td class="px-4 py-2">
							{item.product.price != null
								? `sFr. ${(item.product.price * item.quantity).toFixed(2)}`
								: '—'}
						</td>
						<td class="px-4 py-2">
							<button
								class="rounded bg-red-700 px-2 py-1 text-sm text-white transition hover:bg-yellow-400 hover:text-gray-900"
								onclick={() => removeFromCart(item.product.id)}
							>delete</button>
						</td>
					</tr>
				{/each}
			</tbody>
			<tfoot>
				<tr class="font-bold">
					<td colspan="5" class="px-4 py-2 text-right">Total</td>
					<td class="px-4 py-2">sFr. {total.toFixed(2)}</td>
				</tr>
			</tfoot>
		</table>

		<div class="mt-6 mb-8 flex gap-4">
			<button
				class="rounded bg-slate-400 px-4 py-2 text-white transition hover:bg-gray-900"
				onclick={() => { clearCart(); goto('/product/shop'); }}
			>Cancel</button>
			<button
				class="ml-auto rounded bg-gray-800 px-6 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
				onclick={() => goto('/checkout')}
			>Checkout →</button>
		</div>
	{/if}
</div>
