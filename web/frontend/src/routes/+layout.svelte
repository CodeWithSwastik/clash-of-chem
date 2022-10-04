<script>
  	import "../app.css";
</script>

<div class="app bg-dark">
	<nav class="flex p-2 absolute">
		<a href="/" class="px-3 py-1 bg-gray-200 rounded-full">Home</a>
	</nav>
	<main>
		<slot />
	</main>
</div>

<style>
</style>