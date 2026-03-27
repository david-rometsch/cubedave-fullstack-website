<script>
	import { cart, clearCart } from '$lib/cart.svelte.js';
	import { checkout } from '$lib/checkout.svelte.js';
	import Stepper from '$lib/Stepper.svelte';
	import { goto } from '$app/navigation';
	import { toast } from 'svelte-sonner';

	const total = $derived(
		cart.reduce((sum, i) => sum + (i.product.price ?? 0) * i.quantity, 0)
	);

	const paymentLabels = { card: 'Credit Card', twint: 'TWINT', invoice: 'Invoice' };

	let showPayment = $state(false);
	let progress = $state(0);

	function startPayment() {
		if (!checkout.firstName.trim() || !checkout.lastName.trim() || !checkout.email.trim()) {
			toast.error('Please fill in first name, last name and email.');
			return;
		}
		if (cart.length === 0) {
			toast.error('Your cart is empty.');
			return;
		}

		showPayment = true;
		// Trigger CSS transition on next tick
		setTimeout(() => { progress = 100; }, 50);

		setTimeout(async () => {
			const customerName = `${checkout.firstName} ${checkout.lastName}`;
			const res = await fetch('/api/orders', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					customer_name: customerName,
					items: cart.map((i) => ({ product_id: i.product.id, quantity: i.quantity }))
				})
			});

			if (res.ok) {
				checkout.confirmedOrder = {
					customerName,
					paymentMethod: checkout.paymentMethod,
					items: cart.map((i) => ({
						name: i.product.name,
						price: i.product.price,
						image: i.product.image ?? null,
						quantity: i.quantity
					})),
					total
				};
				clearCart();
				goto('/confirmation');
			} else {
				showPayment = false;
				progress = 0;
				toast.error('Payment failed. Please try again.');
			}
		}, 3000);
	}
</script>

<div class="mx-auto max-w-5xl px-6 py-8">
	<Stepper step="checkout" />

	<div class="mt-8 flex gap-0">
		<!-- ── Left: form ── -->
		<div class="flex-1 pr-10">
			<h2 class="mb-5 text-lg font-semibold text-gray-800">Your Details</h2>

			<!-- First + Last name side by side -->
			<div class="mb-4 flex gap-4">
				<div class="flex-1">
					<label class="mb-1 block text-sm text-gray-500">First Name *</label>
					<input
						type="text"
						bind:value={checkout.firstName}
						placeholder="Jane"
						class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
					/>
				</div>
				<div class="flex-1">
					<label class="mb-1 block text-sm text-gray-500">Last Name *</label>
					<input
						type="text"
						bind:value={checkout.lastName}
						placeholder="Smith"
						class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
					/>
				</div>
			</div>

			<div class="mb-4">
				<label class="mb-1 block text-sm text-gray-500">Email *</label>
				<input
					type="email"
					bind:value={checkout.email}
					placeholder="jane@example.com"
					class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
				/>
			</div>

			<div class="mb-4">
				<label class="mb-1 block text-sm text-gray-500">Street &amp; Number</label>
				<input
					type="text"
					bind:value={checkout.address}
					placeholder="Example Street 1"
					class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
				/>
			</div>

			<!-- ZIP + City side by side -->
			<div class="mb-8 flex gap-4">
				<div class="w-28">
					<label class="mb-1 block text-sm text-gray-500">ZIP</label>
					<input
						type="text"
						bind:value={checkout.zip}
						placeholder="8000"
						class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
					/>
				</div>
				<div class="flex-1">
					<label class="mb-1 block text-sm text-gray-500">City</label>
					<input
						type="text"
						bind:value={checkout.city}
						placeholder="Zurich"
						class="w-full rounded border border-gray-300 px-3 py-2 outline-none focus:border-gray-800"
					/>
				</div>
			</div>

			<!-- Payment method -->
			<h2 class="mb-4 text-lg font-semibold text-gray-800">Payment Method</h2>
			<div class="mb-10 flex flex-col gap-2">
				{#each [{ value: 'card', label: 'Credit Card' }, { value: 'twint', label: 'TWINT' }, { value: 'invoice', label: 'Invoice' }] as method}
					<label
						class="flex cursor-pointer items-center gap-3 rounded border px-4 py-3 transition
							{checkout.paymentMethod === method.value
							? 'border-gray-800 bg-gray-50'
							: 'border-gray-200 hover:border-gray-400'}"
					>
						<input
							type="radio"
							bind:group={checkout.paymentMethod}
							value={method.value}
							class="h-4 w-4 accent-gray-800"
						/>
						<span class="text-gray-700">{method.label}</span>
					</label>
				{/each}
			</div>

			<div class="mt-2 flex items-center gap-4">
				<a
					href="/shopping-cart"
					class="rounded bg-slate-400 px-5 py-3 text-white transition hover:bg-gray-900"
				>
					back</a
				>
				<button
					class="ml-auto rounded bg-gray-800 px-8 py-3 text-white transition hover:bg-yellow-400 hover:text-gray-900"
					onclick={startPayment}
					>payment
				</button>
			</div>
		</div>

		<!-- ── Right: order summary ── -->
		<div class="shrink-0 border-l border-gray-200 pl-10" style="width:22rem">
			<div class="sticky top-4">
				<h2 class="mb-4 text-sm font-semibold tracking-wide text-gray-500 uppercase">Your Order</h2>
				{#each cart as item}
					<div class="mb-4 flex items-center gap-3">
						{#if item.product.image}
							<img
								src={item.product.image}
								alt={item.product.name}
								class="h-12 w-12 shrink-0 rounded object-contain"
							/>
						{:else}
							<div class="h-12 w-12 shrink-0 rounded bg-gray-200"></div>
						{/if}
						<div class="flex flex-1 justify-between gap-2 text-sm text-gray-700">
							<span>{item.quantity}× {item.product.name}</span>
							<span class="shrink-0 font-medium">
								{item.product.price != null
									? `sFr. ${(item.product.price * item.quantity).toFixed(2)}`
									: '—'}
							</span>
						</div>
					</div>
				{/each}
				<div
					class="mt-2 flex justify-between border-t border-gray-200 pt-4 font-semibold text-gray-800"
				>
					<span>Total</span>
					<span>sFr. {total.toFixed(2)}</span>
				</div>
				<a
					href="/shopping-cart"
					class="mt-4 block text-center text-xs text-gray-400 transition hover:text-gray-700"
					>Edit cart</a
				>
			</div>
		</div>
	</div>
</div>

<!-- ── Payment processing popup ── -->
{#if showPayment}
	<div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
		<div class="w-96 rounded-lg bg-white p-8 shadow-xl">
			<h2 class="mb-1 text-lg font-semibold text-gray-800">Processing payment…</h2>
			<p class="mb-6 text-sm text-gray-400">Please wait a moment.</p>
			<div class="h-2 w-full overflow-hidden rounded-full bg-gray-200">
				<div
					class="h-full rounded-full bg-gray-800 transition-all ease-linear"
					style="width:{progress}%; transition-duration:3000ms"
				></div>
			</div>
		</div>
	</div>
{/if}
