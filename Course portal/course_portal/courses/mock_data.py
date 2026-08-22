COURSES = {

    'PY101': {
        'meta': {
            'title': 'Core Python',
            'level': 'beginner',
            'price': 3000,
            'duration': 150,
        },
        'instructor': {
            'name': 'Giridhar',
            'experience': 8,
            'info': 'Python developer and programming instructor'
        },
        'modules': [
            'prerequisites', 'basics of python', 'programming',
            'object oriented', 'exception handling', 'file handling', 'collections'
        ]
    },

    'DJ201': {
        'meta': {
            'title': 'Django Web Development',
            'level': 'intermediate',
            'price': 5000,
            'duration': 180,
        },
        'instructor': {
            'name': 'Rahul Sharma',
            'experience': 7,
            'info': 'Backend developer specializing in Django'
        },
        'modules': [
            'python revision', 'django basics', 'urls and views',
            'templates', 'models', 'forms', 'authentication', 'rest api'
        ]
    },

    'JS101': {
        'meta': {
            'title': 'JavaScript Fundamentals',
            'level': 'beginner',
            'price': 2800,
            'duration': 140,
        },
        'instructor': {
            'name': 'Priya Mehta',
            'experience': 6,
            'info': 'Frontend developer and JavaScript instructor'
        },
        'modules': [
            'javascript basics', 'variables', 'functions',
            'arrays', 'objects', 'dom', 'events', 'async javascript'
        ]
    },

    'RE201': {
        'meta': {
            'title': 'React Development',
            'level': 'intermediate',
            'price': 4500,
            'duration': 170,
        },
        'instructor': {
            'name': 'Ankit Verma',
            'experience': 8,
            'info': 'React developer with experience in modern frontend applications'
        },
        'modules': [
            'react basics', 'components', 'jsx', 'props',
            'state', 'hooks', 'forms', 'routing', 'api integration'
        ]
    },

    'HT101': {
        'meta': {
            'title': 'HTML and CSS',
            'level': 'beginner',
            'price': 2200,
            'duration': 120,
        },
        'instructor': {
            'name': 'Neha Joshi',
            'experience': 5,
            'info': 'Frontend developer and UI design instructor'
        },
        'modules': [
            'html basics', 'semantic html', 'forms',
            'css basics', 'box model', 'flexbox', 'grid', 'responsive design'
        ]
    },

    'SQL201': {
        'meta': {
            'title': 'SQL and Database Management',
            'level': 'beginner',
            'price': 3200,
            'duration': 145,
        },
        'instructor': {
            'name': 'Vikram Singh',
            'experience': 9,
            'info': 'Database engineer and SQL trainer'
        },
        'modules': [
            'database basics', 'sql basics', 'select queries',
            'joins', 'subqueries', 'aggregate functions',
            'constraints', 'indexes', 'normalization'
        ]
    },

    'DSA201': {
        'meta': {
            'title': 'Data Structures and Algorithms',
            'level': 'intermediate',
            'price': 5500,
            'duration': 220,
        },
        'instructor': {
            'name': 'Arjun Kapoor',
            'experience': 10,
            'info': 'Software engineer and competitive programming mentor'
        },
        'modules': [
            'complexity', 'arrays', 'strings', 'linked lists',
            'stacks', 'queues', 'trees', 'graphs', 'sorting', 'searching'
        ]
    },

    'JAVA101': {
        'meta': {
            'title': 'Core Java',
            'level': 'beginner',
            'price': 3500,
            'duration': 160,
        },
        'instructor': {
            'name': 'Suresh Kumar',
            'experience': 11,
            'info': 'Java developer and enterprise application trainer'
        },
        'modules': [
            'java basics', 'variables', 'methods', 'arrays',
            'oops', 'inheritance', 'interfaces', 'exceptions', 'collections'
        ]
    },

    'SPR301': {
        'meta': {
            'title': 'Spring Boot',
            'level': 'advanced',
            'price': 6000,
            'duration': 200,
        },
        'instructor': {
            'name': 'Amit Malhotra',
            'experience': 12,
            'info': 'Backend engineer specializing in Java and Spring'
        },
        'modules': [
            'spring basics', 'spring boot', 'dependency injection',
            'rest controllers', 'jpa', 'hibernate',
            'security', 'database integration', 'microservices'
        ]
    },

    'GIT101': {
        'meta': {
            'title': 'Git and GitHub',
            'level': 'beginner',
            'price': 1800,
            'duration': 80,
        },
        'instructor': {
            'name': 'Rohan Patel',
            'experience': 6,
            'info': 'Software engineer and version control trainer'
        },
        'modules': [
            'git basics', 'repositories', 'commits',
            'branches', 'merging', 'conflicts', 'github',
            'pull requests', 'collaboration'
        ]
    },

    'NODE201': {
        'meta': {
            'title': 'Node.js Backend Development',
            'level': 'intermediate',
            'price': 4200,
            'duration': 160,
        },
        'instructor': {
            'name': 'Karan Gupta',
            'experience': 7,
            'info': 'Backend developer specializing in Node.js'
        },
        'modules': [
            'node basics', 'modules', 'npm',
            'express', 'routing', 'middleware',
            'rest api', 'authentication', 'mongodb'
        ]
    },

    'FL101': {
        'meta': {
            'title': 'Flask Web Development',
            'level': 'intermediate',
            'price': 3800,
            'duration': 140,
        },
        'instructor': {
            'name': 'Meera Shah',
            'experience': 6,
            'info': 'Python backend developer and Flask instructor'
        },
        'modules': [
            'flask basics', 'routing', 'templates',
            'forms', 'database', 'rest api',
            'authentication', 'deployment'
        ]
    },

    'TS201': {
        'meta': {
            'title': 'TypeScript',
            'level': 'intermediate',
            'price': 3000,
            'duration': 120,
        },
        'instructor': {
            'name': 'Pooja Nair',
            'experience': 7,
            'info': 'Frontend engineer specializing in TypeScript'
        },
        'modules': [
            'typescript basics', 'types', 'interfaces',
            'functions', 'classes', 'generics',
            'enums', 'modules', 'react with typescript'
        ]
    },

    'WEB301': {
        'meta': {
            'title': 'Full Stack Web Development',
            'level': 'advanced',
            'price': 7500,
            'duration': 260,
        },
        'instructor': {
            'name': 'Vivek Rao',
            'experience': 13,
            'info': 'Full stack engineer and technical mentor'
        },
        'modules': [
            'html css', 'javascript', 'react',
            'backend development', 'rest api', 'databases',
            'authentication', 'deployment', 'project development'
        ]
    },

    'CLOUD201': {
        'meta': {
            'title': 'Cloud Computing Fundamentals',
            'level': 'beginner',
            'price': 4000,
            'duration': 150,
        },
        'instructor': {
            'name': 'Nitin Yadav',
            'experience': 9,
            'info': 'Cloud engineer and infrastructure trainer'
        },
        'modules': [
            'cloud basics', 'virtual machines', 'storage',
            'networking', 'databases', 'security',
            'scalability', 'cloud deployment'
        ]
    }

}