# XDC 2021

Files used to stream the X Developers Conference 2021, along with most graphics and OBS Studio data.
To play with this, you'll need:

- [OBS Studio](https://obsproject.com/) for scenes, streaming, etc
- [Iosevka fonts (TTF)](https://github.com/be5invis/Iosevka/releases)
- [Krita](https://krita.org/) for .kra graphics
- [Inkscape](https://inkscape.org/) for .svg graphics

You can learn more about the conference on [its homepage](https://xdc2021.x.org/).

Please steal. :)

## Details

In general, the setup is not that far away from what was done in the previous year, see:

- Last year's [ivyl's blog](https://blog.hiler.eu/xdc-2020/)
- Last year's [mupuf's blog](https://mupuf.org/blog/2020/09/28/3-ways-to-host-a-conference-using-jitsi/)
- Music: Jeremy Blake - Through The Crystal ([from YouTube Audio Library](https://www.youtube.com/audiolibrary) and not redistributable)
- Slides for [How we did XDC 2021](https://indico.freedesktop.org/event/1/contributions/46/attachments/29/39/TechStuff.pdf) for infra/services overview
- Lock down YouTube comments - there's a "force review" mode on all new comments available. I missed that on day 1 and regretted it.
- OBS scenes in use are in this repo. We had two OBS instances, primary running talks and backup running workshops.
- There was no 3rd OBS setup to switch between those - instead, each streamed to a Nginx RTMP box, which forwarded the stream to YouTube and media.ccc.de (thank you!) - Nginx config is in the repo.
- For media.ccc.de, you need a [config](https://github.com/voc/streaming-website/tree/master/configs/conferences/xdc2021) and the fahrplan XML from [this converter](https://github.com/voc/voctosched/pull/45)
- We hosted Jitsi and the RTMP gateway on Hetzner with their CPX31 instances. It cost us ~5 EUR total for all 3 days (and maybe 1EUR extra for testing before the conf).


## Nice to haves

- A single person streaming for 6-7 hours straight is a bit much - having someone to switch halfway through the day would be nice but wasn't so easy to coordinate online. (The 3rd OBS setup from the last year would've helped here :D)
- I wanted an animated background live from Godot, but running that caused some frame drops in OBS when also running Jitsi - so back to the static background we went.
- Automate everything - we had a handy switcher to quickly swap the next talk/presenter name, but having that automated so that it'd switch automatically would help, too. OBS has built-in scripting and we used it for powerline-like details - it should be possible to fully automate title changes too.
