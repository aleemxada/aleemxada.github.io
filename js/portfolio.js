(function () {
  'use strict';

  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('is-open');
    });
  }

  const projectGrid = document.getElementById('project-grid');
  if (projectGrid && typeof PROJECT_LIST !== 'undefined') {
    const domainClass = {
      EdTech: 'domain-edtech',
      FinTech: 'domain-fintech',
      Logistics: 'domain-logistics',
      'E-Commerce': 'domain-ecommerce',
      'B2B SaaS': 'domain-b2b',
      'B2B / Manufacturing': 'domain-b2b',
      'FinTech / AI': 'domain-fintech',
      'SaaS / Community': 'domain-b2b',
      'Compliance / Industrial': 'domain-logistics',
      'Operations / HR': 'domain-b2b',
      'Marketplace / Mobile': 'domain-ecommerce'
    };

    PROJECT_LIST.forEach(function (project) {
      const card = document.createElement('article');
      card.className = 'repo-card';
      const domainCls = domainClass[project.domain] || '';
      const excerpt = project.excerpt || project.tagline;
      const prodBadge = project.production_url
        ? ' <span class="visibility" style="color:var(--gh-success)">● live</span>'
        : '';
      const tags = project.stack.slice(0, 4).map(function (t) {
        return '<span class="tag ' + domainCls + '">' + t + '</span>';
      }).join('');

      card.innerHTML =
        '<h3><a href="projects/' + project.slug + '.html">' + project.title + '</a>' +
        '<span class="visibility">' + project.domain + '</span>' + prodBadge + '</h3>' +
        '<p class="repo-desc">' + project.tagline + '</p>' +
        '<p class="repo-excerpt">' + excerpt + '</p>' +
        '<div class="repo-meta">' +
        '<span class="repo-lang"><span class="lang-dot laravel"></span> Laravel</span>' +
        '<a href="projects/' + project.slug + '.html" class="repo-cta">Read case study →</a>' +
        '</div>' +
        '<div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:6px">' + tags + '</div>';

      projectGrid.appendChild(card);
    });
  }

  const contribGraph = document.getElementById('contrib-graph');
  if (contribGraph) {
    for (let i = 0; i < 52 * 7; i++) {
      const cell = document.createElement('span');
      cell.className = 'contrib-cell l' + (Math.random() > 0.35 ? Math.floor(Math.random() * 4) + 1 : '');
      contribGraph.appendChild(cell);
    }
  }
})();
