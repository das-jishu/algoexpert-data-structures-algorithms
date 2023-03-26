// calendar1  = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
// dailyBounds1  = ['9:00', '20:00'];
// calendar2  = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
// dailyBounds2  = ['10:00', '18:30'];
// meetingDuration = 30;

// Sample Output =  = ['10:00', '18:30'];

// O(c1 + c2) time | O(c1 + c2) space - where c1 and c2 are the respective numbers of meetings
// in calendar 1 and calendar2

function calendarMatching(
  calendar1,
  dailyBounds1,
  calendar2,
  dailyBounds2,
  meetingDuration
) {
  const updatedCalendar1 = updateCalendar(calendar1, dailyBounds1);
  const updatedCalendar2 = updateCalendar(calendar2, dailyBounds2);
  const mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2);
  const flattenedCalendar = flattenCalendar(mergedCalendar);
  return getMatchingAvailabilities(flattenedCalendar, meetingDuration);
}

function getMatchingAvailabilities(flattenCalendar, meetingDuration) {
  // flattenedCalendar = [[0, 120], [120, 180], [250, 300]];
  let availabilities = [];

  for (let i = 1; i < flattenCalendar.length; i++) {
    const previousFinish = flattenCalendar[i - 1][1];
    const currentStart = flattenCalendar[i][0];

    if (currentStart - previousFinish >= meetingDuration) {
      availabilities.push([previousFinish, currentStart]);
    }
  }

  return availabilities.map((a) => a.map((minutes) => minutesToTime(minutes)));
}

function flattenCalendar(calendar) {
  // Merged calendar = [[0, 120], [10, 90], [80, 120], [150, 200]]
  let flattened = [calendar[0]];

  for (let i = 1; i < calendar.length; i++) {
    const previousMeeting = flattened[flattened.length - 1];
    const currentMeeting = calendar[i];
    const [previousStart, previousFinish] = previousMeeting;
    const [currentStart, currentFinish] = currentMeeting;

    if (previousFinish >= currentStart) {
      flattened[flattened.length - 1] = [
        previousStart,
        Math.max(currentFinish, previousFinish),
      ];
    } else {
      flattened.push(currentMeeting);
    }
  }

  return flattened;
}

function mergeCalendars(calendar1, calendar2) {
  let merged = [];
  let i = 0;
  let j = 0;

  while (i < calendar1.length && j < calendar2.length) {
    const meeting1 = calendar1[i];
    const meeting2 = calendar2[j];

    if (meeting1[0] < meeting2[0]) {
      merged.push(meeting1);
      i++;
    } else {
      merged.push(meeting2);
      j++;
    }
  }

  while (i < calendar1.length) {
    merged.push(calendar1[i]);
    i++;
  }
  while (j < calendar2.length) {
    merged.push(calendar2[j]);
    j++;
  }

  return merged;
}

function updateCalendar(calendar, dailyBounds) {
  const updatedCalendar = [
    ['0:00', dailyBounds[0]],
    ...calendar,
    [dailyBounds[1], '23:59'],
  ];
  return updatedCalendar.map((cal) => cal.map((time) => timeToMinutes(time)));
}

function timeToMinutes(time) {
  const [hour, min] = time.split(':').map((s) => parseInt(s));
  return hour * 60 + min;
}

function minutesToTime(minutes) {
  const hour = Math.floor(minutes / 60);
  const min = minutes % 60;

  const minString = min < 10 ? '0' + min : min.toString();

  return hour + ':' + minString;
}
// Do not edit the line below.
exports.calendarMatching = calendarMatching;
