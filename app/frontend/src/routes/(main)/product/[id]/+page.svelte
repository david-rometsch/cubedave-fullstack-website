<script>
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import { cart, addToCart } from '$lib/cart.svelte.js';
	import { products, loadProducts } from '$lib/products.svelte.js';

	const id = page.params.id;
	let quantity = $state(1);
	let activeImage = $state(null);

	onMount(loadProducts);

	const product = $derived(products.find((p) => p.id == id) ?? null);

	// All non-null images in order
	const images = $derived(
		product ? [product.image, product.image2, product.image3].filter(Boolean) : []
	);

	// Reset active image whenever the product changes
	$effect(() => {
		activeImage = product?.image ?? null;
	});
</script>

<a href="/product/shop" class="mt-4 inline-block px-6 text-gray-500 hover:text-gray-900">← Shop</a>

{#if product}
	<div class="mx-auto mt-8 max-w-2xl px-6">
		<div class="flex gap-8">
			<!-- ── Image viewer ── -->
			<div class="flex-shrink-0">
				<!-- Main image -->
				{#if activeImage}
					<img src={activeImage} alt={product.name} class="h-48 w-48 rounded object-contain" />
				{:else}
					<div class="flex h-48 w-48 items-center justify-center rounded bg-gray-100 text-sm text-gray-400">
						no image
					</div>
				{/if}

				<!-- Thumbnails — only shown when there is more than one image -->
				{#if images.length > 1}
					<div class="mt-3 flex gap-2">
						{#each images as img}
							<button
								onclick={() => (activeImage = img)}
								class="rounded border-2 p-0.5 transition
									{activeImage === img
									? 'border-gray-800'
									: 'border-transparent hover:border-gray-300'}"
							>
								<img src={img} alt="" class="h-14 w-14 rounded object-contain" />
							</button>
						{/each}
					</div>
				{/if}
			</div>

			<!-- ── Product info ── -->
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
					<select class="w-14 rounded border border-gray-300 py-1 pr-6 pl-2" bind:value={quantity}>
						{#each [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] as n}
							<option value={n}>{n}</option>
						{/each}
					</select>
					<button
						class="rounded bg-gray-800 px-4 py-2 text-white transition hover:bg-yellow-400 hover:text-gray-900"
						onclick={() => addToCart(product, quantity)}>add</button
					>
				</div>
			</div>
		</div>

		{#if product.description}
			<div class="prose mt-8 max-w-none leading-relaxed text-gray-700">
				{@html product.description}
			</div>
		{/if}
	</div>
{/if}
