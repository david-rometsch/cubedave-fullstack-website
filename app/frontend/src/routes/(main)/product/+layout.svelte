<script>
	let { children } = $props();
</script>

<!-- 2nd navbar: shop title -->
<nav class="bg-gray-900 px-6 py-3">
	<ul class="flex items-center gap-6">
		<li class="text-2xl font-bold text-yellow-400">Get Cubes at CubeDave's Cube Shop</li>
	</ul>
</nav>

{@render children()}
