<script>
    // @ts-nocheck
    export let username, color;

    let colors = {
        'rosewater': "#f5e0dc",
        'pink': "#f5c2e7", 
        'maroon': "#eba0ac", 
        'peach': "#fab387", 
        'yellow': "#f9e2af", 
        'teal': "#94e2d5", 
        'sky': "#89dceb", 
        'lavender': "#b4befe"
    };
    let pfpcolor = colors[color];
</script>

<div class="min-w-[50px] p-5 bg-mantle rounded shadow-lg shadow-gray-900">
    <div class="text-center text-5xl">
        <i class="fa-solid fa-user" style="color: {pfpcolor};"/>
    </div>
    <div class="text-center mt-2" style="color: {pfpcolor};">{username}</div>
</div>
