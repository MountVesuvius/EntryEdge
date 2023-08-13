<script>
    import Chip from "./Chip.svelte";

    export let color = "#DAF5ED";
    export let company = "Amazon";
    export let title = "Senior UI/UX Designer";
    export let jobLink = "https://www.seek.com.au/";
    export let description = "Nisi laboris qui laborum sunt irure veniam eiusmod officia do quis exercitation aliqua. Nisi laboris qui laborum sunt irure veniam ";
    // export let area = "Computer Science";
    export let companyImg = "https://assets.aboutamazon.com/dims4/default/47b2485/2147483647/strip/true/crop/198x73+0+0/resize/300x111!/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2Fd7%2F46%2F57d4c6d54c5bafd771a85f5058fe%2Ffire-tablet-0.jpg";

    let isBookmarkActive = false;
</script>

<div class="bg-white my-3 sm:m-3 rounded-xl p-3 w-[95vw] sm:w-96" style="font-family: 'Nunito';">
    <section class="p-3 rounded-xl min-h-80 h-80 flex flex-col justify-start" style="background-color: {color}">
        <div class="flex justify-between">
            <div class="w-72">
                <span class="font-bold ">{company}</span>
                <h2 class="font-extrabold text-2xl">{title}</h2>
            </div>
            <button on:click={() => {isBookmarkActive = !isBookmarkActive}} class="w-8 h-8 rounded-full bg-white flex items-center justify-center">
                {#if isBookmarkActive}
                <img src="icons/bookmark_filled.svg" alt="bookmark">
                {:else}
                <img src="icons/bookmark.svg" alt="bookmark">
                {/if}
            </button>
        </div>
        <p class="w-72 sm:w-80 max-h-80 overflow-hidden">{description}</p>
        <!-- <div> -->
            <!-- <Chip content={area}/> -->
        <!-- </div> -->
    </section>

    <div class="flex justify-between items-center mr-4 mt-2">
        <img src={companyImg} alt="company logo" class="rounded-md object-contain h-20 w-24 justify-self-start">
        <a href={jobLink}><button class="bg-black text-white px-6 py-4 rounded-full">Details</button></a>
    </div>
</div>
