<script>
    import Posting from "$lib/components/Posting.svelte";
    import jobs from '$lib/data/jobs.json';

    const colors = [
        "#FFE1CC", 
        "#FFD1E8", 
        "#E1FFD1", 
        "#CCF5FF", 
        "#FFCCF2", 
        "#F2DFFF", 
        "#E0E4FF", 
        "#D5FFFB", 
        "#FFFAE1", 
    ]

    function pickRandomColor() {
        let picked = colors[Math.floor(Math.random() * colors.length)];
        colors.splice(colors.indexOf(picked), 1);
        return picked;
    }

</script>

<div class="w-screen flex flex-col items-center justify-center text-center text-white mb-6">
    <h1 class="text-[1.5rem] sm:text-[4rem] font-bold">Find Your First Student Job</h1>
    <h3 class="sm:text-[2rem]">Launching your careers, the right way</h3>
</div>

<!-- filters -->
<!-- <div class="">

</div> -->


<div class="flex flex-col flex-wrap sm:flex-row mx-4 justify-center">
    {#each jobs.jobPostings as job}
        <Posting
            color={pickRandomColor()}
            date={job.postedDate}
            company={job.company}
            title={job.title}
            location={job.location}
            salary={job.hourlyRate}
            tags={job.tags}
        />
    {/each}
</div>