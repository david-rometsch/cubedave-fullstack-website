<script>
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import { addToCart } from '$lib/cart.svelte.js';
	import { products, loadProducts } from '$lib/products.svelte.js';

	// Read dynamic route segment — e.g. /product/3 → id = "3"
	const id = page.params.id;
	let quantity = $state(1);

	onMount(loadProducts);

	// Derived from the shared store — no extra fetch needed if already cached
	const product = $derived(products.find((p) => p.id == id) ?? null);
</script>

<a href="/" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Shop</a>

{#if product}
	<div class="mx-auto mt-8 max-w-2xl px-6">
		<div class="flex gap-8">
			<div class="flex-shrink-0">
				{#if product.image}
					<img src={product.image} alt={product.name} class="h-48 w-48 rounded object-contain" />
				{:else}
					<div class="flex h-48 w-48 items-center justify-center rounded bg-gray-100 text-sm text-gray-400">
						kein Bild
					</div>
				{/if}
			</div>
			<div class="flex flex-col gap-2">
				<h1 class="text-3xl font-bold">{product.name}</h1>
				<p class="text-gray-500">{product.brand} · {product.size} · {product.category}</p>
				{#if product.info}
					<p class="text-sm text-gray-400">{product.info}</p>
				{/if}
				<p class="mt-2 text-2xl font-bold text-gray-900">
					{product.price != null ? `sFr. ${product.price.toFixed(2)}` : '—'}
				</p>
				<div class="mt-4 flex items-center gap-3">
					<select
						class="w-14 rounded border border-gray-300 py-1 pl-2 pr-6"
						bind:value={quantity}
					>
						{#each [1,2,3,4,5,6,7,8,9,10] as n}
							<option value={n}>{n}</option>
						{/each}
					</select>
					<button
						class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
						onclick={() => addToCart(product, quantity)}
					>add</button>
				</div>
			</div>
		</div>
		{#if product.description}
			<p class="mt-8 leading-relaxed text-gray-700">{product.description}</p>
		{/if}
	</div>
{/if}
