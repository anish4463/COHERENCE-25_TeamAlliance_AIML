document.addEventListener('DOMContentLoaded', function() {
    // Sample career paths data (in production, this would come from your AI backend)
    const careerPaths = {
        'software-engineer': {
            paths: [
                {
                    title: 'Technical Leadership',
                    progression: ['Senior Engineer', 'Tech Lead', 'Engineering Manager', 'CTO'],
                    probability: 0.85,
                    timeframe: '5-7 years'
                },
                {
                    title: 'AI Specialization',
                    progression: ['ML Engineer', 'AI Architect', 'AI Research Lead'],
                    probability: 0.75,
                    timeframe: '3-5 years'
                },
                {
                    title: 'Product Focus',
                    progression: ['Product Engineer', 'Product Manager', 'Director of Product'],
                    probability: 0.65,
                    timeframe: '4-6 years'
                }
            ],
            skills: {
                current: ['JavaScript', 'Python', 'React', 'Node.js'],
                recommended: ['Machine Learning', 'System Design', 'Team Leadership']
            }
        }
    };

    // Function to update trajectory visualization
    function updateTrajectory(careerPath) {
        const currentProfile = document.querySelector('#currentProfile');
        const projection = document.querySelector('#fiveYearProjection');
        const market = document.querySelector('#marketAlignment');

        // Update growth potential with animation
        const growthElement = document.querySelector('#growthPotential');
        if (growthElement) {
            const targetGrowth = 95;
            let currentGrowth = 0;
            const growthInterval = setInterval(() => {
                if (currentGrowth >= targetGrowth) {
                    clearInterval(growthInterval);
                } else {
                    currentGrowth++;
                    growthElement.textContent = `${currentGrowth}% Growth Potential`;
                }
            }, 20);
        }

        // Add hover effects for detailed info
        const infoCards = document.querySelectorAll('.career-card');
        infoCards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.classList.add('transform', 'scale-105', 'z-10');
            });
            card.addEventListener('mouseleave', function() {
                this.classList.remove('transform', 'scale-105', 'z-10');
            });
        });
    }

    // Initialize trajectory visualization
    updateTrajectory('software-engineer');

    // Add click handlers for different career paths
    document.querySelectorAll('.career-path-option').forEach(option => {
        option.addEventListener('click', function() {
            updateTrajectory(this.dataset.path);
        });
    });
});