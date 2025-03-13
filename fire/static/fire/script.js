document.addEventListener('DOMContentLoaded', () => {

    // Message Sent Toast
    const toastLiveExample = document.getElementById('liveToast')
    const status = toastLiveExample.getAttribute('data-messageSent')

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    if (status != 'False') {
        toastBootstrap.show()
    }

    window.addEventListener('load', (event) => {
        //Hero CTA animation
        const cta_animation = document.getElementById('cta_animation');
        const svgatorDocumentD = cta_animation.contentDocument || cta_animation.contentWindow.document;
        const svgatorElementD = svgatorDocumentD.getElementById('e5o69M3Cie81');
        const heroBtn = document.querySelector('#heroBtn')
        heroBtn.addEventListener('mouseover', () => svgatorElementD.svgatorPlayer.play())
        heroBtn.addEventListener('mouseout', () => svgatorElementD.svgatorPlayer.stop())
        })
})