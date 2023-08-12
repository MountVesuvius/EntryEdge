<script>
    import Chip from "./Chip.svelte";

    export let color = "#DAF5ED";
    export let date = "20 May, 2023";
    export let company = "Amazon";
    export let title = "Senior UI/UX Designer";
    export let salary = "$250";
    export let location = "Melbourne, Australia";
    export let tags = ["Part time", "Entry Level", "Remote", "Project work", "Pet Friendly"];
    export let jobLink = "https://www.seek.com.au/";
</script>

<div class="bg-white text-black rounded-xl p-2 mb-3 mx-2 sm:w-96" style="font-family: 'Nunito';" >
    <section class="rounded-xl px-3 py-4 h-64 flex flex-col justify-between" style="background-color: {color}">
        <div>
            <div class="flex justify-between mb-5">
                <span class="bg-white rounded-full px-3 py-1 font-bold">{date}</span>
                <div class="bg-white rounded-full w-8 h-8 flex justify-center items-center"><img src="icons/bookmark.svg" alt="bookmark" class="scale-75"></div>
            </div>

            <div class="flex justify-between items-center ml-1 mb-3">
                    <div>
                        <span class="font-bold">{company}</span>
                        <h2 class="text-2xl font-bold w-48 sm:w-64">{title}</h2>
                    </div>
                    <div class="w-10 h-10 bg-white rounded-full"/>
            </div>
        </div>

        <div class="flex justify-start flex-wrap">
            {#each tags as item}
                <Chip content={item}/>
            {/each}
        </div>
    </section>

    <section class="p-3 flex justify-between">
        <div class="flex flex-col">
            <span class="font-black">{salary}/hr</span>
            <span class="text-sm text-gray-400">{location}</span>
        </div>
        <button class="bg-black text-white rounded-full px-6 hover:bg-zinc-800 transition ease-in-out" ><a href={jobLink}>Details</a></button>
    </section>
</div>