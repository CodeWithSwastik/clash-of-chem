<script lang="ts">
    export let username: string;
</script>

<div class="min-w-[50px] p-5 bg-fg-dark rounded shadow-lg shadow-gray-700">
    <div class="text-center text-5xl">
        <i class="fa-solid fa-user text-gray-400" />
    </div>
    <div class="text-center text-gray-300 mt-2">{username}</div>
</div>