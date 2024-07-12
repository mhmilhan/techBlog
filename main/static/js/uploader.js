tinymce.init({
    selector: "textarea",
    plugins: "insertdatetime media image preview anchor autolink charmap codesample emoticons link lists searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage advtemplate ai mentions tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss markdown",
    toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | alignleft alignright aligncenter alignjustify | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat | preview',

    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',

    mergetags_list: [
        { value: 'First.Name', title: 'First Name' },
        { value: 'Email', title: 'Email' },
    ],

    ai_request: (request, respondWith) => respondWith.string(() => Promise.reject("See docs to implement AI Assistant")),

    image_title: true,
    image_caption: true,
    automatic_uploads: true,
    image_advtab: true,
    file_picker_types: "image media",

    file_picker_callback: function (cb, value, meta) {
        var input = document.createElement("input");
        input.setAttribute("type", "file");
        if (meta.filetype == "image") {
            input.setAttribute("accept", "image/*");
        }
        if (meta.filetype == "media") {
            input.setAttribute("accept", "video/*");
        }

        input.onchange = function () {
            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function () {
                var id = "blobid" + (new Date()).getTime();
                var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                var base64 = reader.result.split(",")[1];
                var blobInfo = blobCache.create(id, file, base64);
                blobCache.add(blobInfo);
                cb(blobInfo.blobUri(), { title: file.name });
            };
            reader.readAsDataURL(file);
        };
        input.click();
    }
});