<template>
  <Layout>
    <div class="flex flex-col items-center w-full">
      <div
        class="bg-white border text-black p-4 lg:p-10 my-8 lg:my-12 mx-auto prose max-w-4xl rounded-lg font-hg border border-purple/15"
        v-html="$page.markdown.content"
      />
    </div>
  </Layout>
</template>

<page-query lang="graphql">
query MarkdownDocs($id: ID!) {
  markdown: markdownDocs(id: $id) {
    id
    path
    description
    title
    content
    fileInfo {
      directory
      extension
      path
      name
    }
  }
}
</page-query>
