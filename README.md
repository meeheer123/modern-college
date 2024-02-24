# modern-college

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link rel="stylesheet" href="style.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />

    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <nav class="navbar mb-5 navbar-shadow navbar-expand-lg bg-body-tertiary">
      <div class="container">
        <!-- <a class="navbar-brand" href="#"><img src="logo.png" alt="logo" /></a> -->
        <a href="navbar-brand" style="text-decoration: none">MedEase</a>
        <button
          class="navbar-toggler bg-white collapsed"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item me-5">
              <a class="nav-link disabled" aria-current="page" href="index.html"
                >Home</a
              >
            </li>

            <li class="nav-item me-5">
              <a class="nav-link active" aria-current="page" href="blogs.html"
                >Blog</a
              >
            </li>
            <li class="nav-item me-5">
              <a class="nav-link active" aria-current="page" href="Contact.html"
                >Contact</a
              >
            </li>
            <li>
              <input
                id="logOut"
                type="button"
                class="btn-primary btn"
                value="Log Out"
              />
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container">
      <div class="row">
        <div class="col-lg-9">
          <div class="container">
            <h2 class="mb-4">Latest Blogs</h2>
            <div class="row">
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/blog_posts/ankylosing-spondylitis/snow_skiers_point_of_view_on_slope/1800x1200_snow_skiers_point_of_view_on_slope.jpg?resize=1024:*&output-quality=20"
                    class="card-img-top" alt="Blog Post 1" />
                  <div class="card-body">
                    <h5 class="card-title">Is the Risk of Injury Worth Pursuing a Passion?</h5>
                    <p class="card-text">
                      If you asked me if I consider myself athletic, my first instinct would be to say no.
                    </p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20240222/is-the-risk-of-injury-worth-pursuing-a-passion" target="_blank"
                      class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/blog_posts/depression/1800x1200_woman_cutting_fresh_vegetables.jpg?resize=1024:*&output-quality=20"
                    class="card-img-top" alt="Blog Post 2" />
                  <div class="card-body">
                    <h5 class="card-title">Struggling to Balance: Finding Time for Self</h5>
                    <p class="card-text">
                      It's no secret that healthy eating and exercise play an important role in managing chronic illness.                </p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20240104/struggling-to-find-balance-finding-time-for-self-care" target="_blank" class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/articles/health_tools/10-ways-watching-tv-gaming-hazardous-to-health/1800ss_getty_rf_back_problems.jpg?resize=800:*"
                    class="card-img-top" alt="Blog Post 3" />
                  <div class="card-body">
                    <h5 class="card-title">When Pain Is the Norm</h5>
                    <p class="card-text">
                      The normal amount of pain is zero?!" When you have a chronic illness, you get so used to a certain level of pain. 
                    </p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20231005/when-pain-is-the-norm" target="_blank" class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/features/_2022/01_2022/plan_and_prepare_for_the_unexpected_migraine_features/1800x1200_plan_and_prepare_for_the_unexpected_migraine_features.jpg?resize=800:*"
                    class="card-img-top" alt="Blog Post 3" />
                  <div class="card-body">
                    <h5 class="card-title">Recognizing AS Milestones</h5>
                    <p class="card-text">
                      Do you remember the day you were diagnosed, the end of your “diagnostic journey”? </p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20230913/recognizing-as-milestones" target="_blank" class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>    
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/blog_posts/ankylosing-spondylitis/1800x1200_birthday_toast_with_string_lights.jpg?resize=800:*"
                    class="card-img-top" alt="Blog Post 3" />
                  <div class="card-body">
                    <h5 class="card-title">Recognizing AS Milestones</h5>
                    <p class="card-text">
                      Living with ankylosing spondylitis, do you thrive and not just survive during holidays?</p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20211228/thriving-during-the-holidays-with-as" target="_blank" class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>    
              <div class="col-md-6 mb-4">
                <div class="card">
                  <img
                    src="https://img.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/blog_posts/ankylosing-spondylitis/1800x1200_doctors_using_digital_tablet_in_hospital.jpg?resize=800:*"
                    class="card-img-top" alt="Blog Post 3" />
                  <div class="card-body">
                    <h5 class="card-title">I’ve Built a Team of Doctors</h5>
                    <p class="card-text">
                      What’s my relationship like with my doctor? Well, it’s complicated. </p>
                    <a href="https://blogs.webmd.com/ankylosing-spondylitis/20230913/recognizing-as-milestones" target="_blank" class="btn btn-primary">Read More</a>
                  </div>
                </div>
              </div>            
            </div>
          </div>
        </div>
        <div class="col-lg-3">
          <h2 class="mb-4">Medi News</h2>
          <div class="card mb-2">
            <div class="card-body">
              <h5 class="card-title">Different types of hair loss: How to recognize the signs and treat it
              </h5>
              <p class="card-text" style="text-overflow:ellipsis; text-align: justify;">Hair loss can be a distressing experience, impacting both physical appearance and emotional well-being. Recognizing the signs and understanding the underlying causes can help individuals seek appropriate treatment and strategies.</p>
              <a href="https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/different-types-of-hair-loss-how-to-recognize-the-signs-and-treat-it/photostory/107943611.cms"
                class="btn btn-primary">Show More</a>
            </div>
          </div>
          <div class="card mb-2">
            <div class="card-body">
              <h5 class="card-title">Increasing Pneumonia Risk: Protect your lungs with these simple tips</h5>
              <p class="card-text">
                COPD or chronic obstructive pulmonary disease is a chronic lung disease that makes it difficult to breathe. It is usually caused by smoking,
</p>
              <a href="https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/increase-pneumonia-risk-protect-your-lungs-with-simple-tips/articleshow/107939394.cms"
                class="btn btn-primary">Show More</a>
            </div>
          </div>
          <div class="card mb-2">
            <div class="card-body">
              <h5 class="card-title">Mobocertinib withdrawal: What it means for people with EGFR+ lung cancer</h5>
              <p class="card-text">EGFR+ lung cancer is a type of lung cancer, not linked to smoking, that is caused by one of a number of nonhereditary gene mutations.</p>
              <a href="https://www.medicalnewstoday.com/articles/mobocertinib-withdrawal-what-it-means-for-people-with-egfr-lung-cancer"
                class="btn btn-primary">Show More</a>
            </div>
          </div>    
        </div>
      </div>
    </div>
    </div>

    <script src="script.js"></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
