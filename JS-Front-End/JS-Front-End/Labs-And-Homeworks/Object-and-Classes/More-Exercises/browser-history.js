function browserHistory(obj, actions) {
    actions.forEach(action => {
        if (action === 'Clear History and Cache') {
            obj['Open Tabs'] = [];
            obj['Recently Closed'] = [];
            obj['Browser Logs'] = [];
        } else {
            let [command, site] = action.split(' ');

            if (command === 'Open') {
                obj['Open Tabs'].push(site);
                obj['Browser Logs'].push(action);
            } else if (command === 'Close') {
                let index = obj['Open Tabs'].indexOf(site);
                if (index > -1) {
                    obj['Open Tabs'].splice(index, 1);
                    obj['Recently Closed'].push(site);
                    obj['Browser Logs'].push(action);
                }
            }
        }
    });

    console.log(`${obj['Browser Name']}`);
    console.log(`Open Tabs: ${obj['Open Tabs'].join(', ')}`);
    console.log(`Recently Closed: ${obj['Recently Closed'].join(', ')}`);
    console.log(`Browser Logs: ${obj['Browser Logs'].join(', ')}`);
}

// Test Case

browserHistory({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
    "Recently Closed":["Yahoo","Gmail"],
    "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
    ["Close Facebook", "Open StackOverFlow", "Open Google"]);
browserHistory({"Browser Name":"Mozilla Firefox",
    "Open Tabs":["YouTube"],
    "Recently Closed":["Gmail", "Dropbox"],
    "Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
    ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]);