<script lang="ts">
    export let username: string;
</script>

<div class="min-w-[50px] p-5 bg-sky rounded shadow-lg shadow-gray-700">
    <div class="text-center text-5xl">
        <i class="fa-solid fa-user text-mantle" />
    </div>
    <div class="text-center text-mantle mt-2">{username}</div>
</div>