# Groups

When your song has multiple phrases that are the same, groups can help avoid repeating the same work multiple times.

## Grouping Notes

Select the notes and select "Merge Into Group" from the right click menu or "Modify" top menu.

![Merge Into Group](/img/advanced/merge-into-group.png)

Once a group has been created, it will be indicated in the Arrangement panel, listed in the Library panel, and have a start marker at the bottom of the Piano Roll.

![Group](/img/advanced/groups.png)

### Managing Groups

Groups can be renamed in the Library panel by double-clicking their name, and can be reordered by dragging the green handle to their left.

![Renaming a Group](/img/advanced/group-rename.png)

A group can be dragged to any point in the Arrangement.

Unlike individual notes, groups can be moved, copied, and pasted within the arrangement panel.

<video width="480" height="360" controls>
    <source src="/img/advanced/drag-group.mp4" type="video/mp4">
    Adding and Moving a Group
</video>

To remove a group from the arrangement, select it and press ++delete++, or delete it from the right click menu.

Even if a group is not present in the arrangement, it will still remain in the Library. To delete a group entirely, right click it and select "Delete Group".

![Deleting an Unused Group](/img/advanced/unused-group.png)

### Modifying a Group

To modify the contents of a group, double-click one of the notes or select the start marker at the bottom of the piano roll.

The area outside the group will be darkened to indicate you are editing the group's contents instead of the track it is part of.

A group can have different voice settings (in the Voice panel) from its parent track. This includes base parameter values, vocal modes, and even a different singer. If these values are not set they will be inherited from the parent track.

![Entering a Group](/img/advanced/group-entered.png)

You can also navigate between groups by right clicking on unoccupied space in the piano roll.

![Navigating Groups by Right Click](/img/advanced/group-enter-rightclick.png)

## Multiple Instances

The same group can exist at multiple points within the arrangement. Each time a group is present is called an "instance" of that group, and all instances are listed in the Library panel along with the respective measures they start in.

Group instances remain linked so that changes to one will affect all the others. This includes changes to the notes as well as parameter curves.

<video width="480" height="360" controls>
    <source src="/img/advanced/group-link.mp4" type="video/mp4">
    Demonstrating Linked Groups
</video>

To remove this linked behavior, right click on one of the groups and select "Dissociate Group".

![Dissociating a Group](/img/advanced/dissociate-group.png)

Once the instance has been dissociated, it will be an instance of a new, separate group and can be modified without influencing the other instances of the original group.

<video width="480" height="360" controls>
    <source src="/img/advanced/modify-group.mp4" type="video/mp4">
    Modifying a Group
</video>

Group instances are treated as separate phrases and therefore do not smoothly transition between one another, even when directly adjacent to notes from another group or the parent track.

## Pitch Offset

If your song has a key change but multiple phrases before and after that point are otherwise identical, you can add a pitch offset to individual instances of the group.

Without entering the group to edit its contents, click and drag the group up or down. The instance will remain linked to the group it is a part of, but will be a certain pitch higher or lower than the other instances.

<video width="640" height="480" controls>
    <source src="/img/advanced/group-pitch-offset.mp4" type="video/mp4">
    Adding a Pitch Offset to a Group
</video>

## Overlapping Groups

Group instances do not interact with the contents of other groups present in the track, or with the contents of the parent track.

Unlike overlapping notes, groups that overlap can produce output simultaneously because they are treated as separate phrases and their synthesized output is calculated separately.

![Overlapping Groups](/img/advanced/overlapping-groups.png)

### Inherited Parameters

The main exception to the above rule is that group instances will inherit any parameter curves from the underlying parent track.

These inherited parameters will only apply to the group instance at the same point on the time axis and will have no effect on instances of the same group elsewhere in the track or project.

<figure markdown>
  ![Inherited Pitch Deviation](/img/advanced/inherited-parameters.png)
  <figcaption>Pitch deviation outside the group affecting one instance's notes.</figcaption>
</figure>

## Video Demonstration

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/kIn3CRfI4xs" title="YouTube video player" frameborder="0" allowfullscreen></iframe>

---

[Report an Issue](https://github.com/claire-west/svstudio-manual/issues/new?template=report-a-problem.md&title=[Page: Groups])