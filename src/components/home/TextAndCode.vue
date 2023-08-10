<template>
  <div class="relative">
    <div class="max-w-6xl w-full mx-auto px-4">
      <div class="flex flex-wrap justify-center lg:justify-between -mx-4">
        <div class="w-full lg:w-5/12 px-4 text-center lg:text-left lg:mb-0 mb-20">
          <h3 class="text-4xl font-bold text-black mb-4">
            Extract, Load and Run <span class="brackets brackets-pink">With Meltano</span>
          </h3>
          <p
            class="text-black/75 opacity-75 text-md leading-relaxed font-grotesk lg:pr-10 tracking-normal my-8"
          >
            Meltano unlocks software development workflows for data movement and gives data engineers
            complete control and visibility of their pipelines, delivering unparalleled efficiency and
            confidence in every change.
          </p>
          <a
            href="#"
            class="bg-blue inline-block font-ibm text-white items-center w-auto rounded-md px-4 py-2.5 border border-blue leading-tight hover:bg-purple hover:border-purple"
            >Explore Meltano</a
          >
        </div>
        <div class="w-full lg:w-7/12 max-w-2xl px-4">
          <div
            class="bg-purple font-ibm text-sm font-normal text-white rounded-md border border-black/15 relative"
          >
            <div class="absolute right-0 -top-1/3 lg:-top-1/2 w-1/3 lg:w-1/3">
              <img src="@/assets/images/meltano-d.svg" alt="Meltano" class="lg:animate-fly" />
            </div>
            <div class="flex flex-row justify-between items-center px-4 py-3">
              <div class="flex flex-row">
                <div class="bg-white/5 border border-white/20 w-3 h-3 rounded-full mx-1"></div>
                <div class="bg-white/5 border border-white/20 w-3 h-3 rounded-full mx-1"></div>
                <div class="bg-white/5 border border-white/20 w-3 h-3 rounded-full mx-1"></div>
              </div>
              <div class="tracking-widest text-white/25">Terminal</div>
              <div class="w-16 flex justify-end">
                <div class="bg-white/5 border border-white/20 w-3 h-3 rounded-full"></div>
              </div>
            </div>
            <div class="px-8 py-6 space-y-6 opacity-90 leading-relaxed border-t border-white/20">
              <p class="mb-6">
                meltano add extractor tap-postgres <br />
                meltano add loader target-snowflake
              </p>
              <p class="mb-6">
                cookiecutter https://github.com/meltano/sdk \ <br />
                <span class="text-green">--directory=</span>"cookiecutter/tap-template" <br />
                <span class="text-grey-medium"># source_name: my-api</span> <br />
                meltano add <span class="text-green">--custom</span> extractor tap-my-api
              </p>
              <p class="mb-6">
                meltano add transformer dbt <br />
                meltano add <span class="text-green">--custom</span> utility my-script.py
              </p>
              <p class="">
                meltano run tap-postgres target-snowflake dbt <br />
                meltano run tap-my-api target-snowflake my-script.py
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="absolute w-72 h-72 top-20 bg-gradient-to-b from-pink via-purple to-blue rounded-full filter blur-[150px] opacity-50 right-0">

</div>
  </div>

</template>
