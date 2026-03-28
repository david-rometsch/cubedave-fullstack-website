<script>
	import { checkout } from '$lib/checkout.svelte.js';
	import Stepper from '$lib/Stepper.svelte';

	const SHIPPING = 6;
	const paymentLabels = { card: 'Credit Card', twint: 'TWINT', invoice: 'Invoice' };
	const order = checkout.confirmedOrder;
</script>

<div class="mx-auto max-w-5xl px-6 py-8">
	<Stepper step="confirmation" passive />

	<div class="mt-8 flex gap-0">
		<!-- ── Left: confirmation message ── -->
		<div class="flex-1 pr-10">
			{#if order}
				<h1 class="mb-3 text-3xl font-bold text-gray-800">Thank you, {order.customerName}!</h1>
				<p class="mb-1 text-gray-600">Your order has been placed successfully.</p>
				<p class="mb-8 text-sm text-gray-400">
					Payment method: {paymentLabels[order.paymentMethod] ?? order.paymentMethod}
				</p>
			{:else}
				<h1 class="mb-3 text-3xl font-bold text-gray-800">Order confirmed!</h1>
				<p class="mb-8 text-gray-600">Thank you for your purchase.</p>
			{/if}

			<a
				href="/product/shop"
				class="rounded bg-gray-800 px-6 py-3 text-white transition hover:bg-yellow-400 hover:text-gray-900"
			>Back to Shop</a>
		</div>

		<!-- ── Right: order summary ── -->
		{#if order}
			<div class="shrink-0 border-l border-gray-200 pl-10" style="width:22rem">
				<h2 class="mb-4 text-sm font-semibold uppercase tracking-wide text-gray-500">Your Order</h2>
				{#each order.items as item}
					<div class="mb-4 flex items-center gap-3">
						{#if item.image}
							<img
								src={item.image}
								alt={item.name}
								class="h-12 w-12 shrink-0 rounded object-contain"
							/>
						{:else}
							<div class="h-12 w-12 shrink-0 rounded bg-gray-200"></div>
						{/if}
						<div class="flex flex-1 justify-between gap-2 text-sm text-gray-700">
							<span>{item.quantity}× {item.name}</span>
							<span class="shrink-0 font-medium">
								{item.price != null
									? `sFr. ${(item.price * item.quantity).toFixed(2)}`
									: '—'}
							</span>
						</div>
					</div>
				{/each}
				<div class="mt-2 flex justify-between border-t border-gray-200 pt-3 text-sm text-gray-500">
					<span>Subtotal</span>
					<span>sFr. {(order.total - SHIPPING).toFixed(2)}</span>
				</div>
				<div class="mt-1 flex justify-between text-sm text-gray-500">
					<span>Shipping</span>
					<span>sFr. {SHIPPING.toFixed(2)}</span>
				</div>
				<div class="mt-2 flex justify-between border-t border-gray-200 pt-3 font-semibold text-gray-800">
					<span>Total</span>
					<span>sFr. {order.total.toFixed(2)}</span>
				</div>
			</div>
		{/if}
	</div>
</div>
