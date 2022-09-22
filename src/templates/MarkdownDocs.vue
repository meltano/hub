<template>
  <Layout>
    <div class="flex flex-col items-center w-full">
      <div
        class="bg-white border text-black p-4 my-7 mx-10 prose max-w-screen-lg rounded-lg"
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
